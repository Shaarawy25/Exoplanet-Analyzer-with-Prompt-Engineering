import requests
import openai
import pandas as pd
import os
from io import StringIO
from dotenv import load_dotenv

load_dotenv()

class ExoplanetAnalyzer:
    def __init__(self):
        self.client = openai.OpenAI(base_url="https://api.groq.com/openai/v1",api_key=os.getenv("GROQ_API_KEY"))
        self.data = self._load_exoplanet_data()
    def _load_exoplanet_data(self):
        url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,hostname,pl_orbper,pl_rade,pl_bmasse,pl_eqt,disc_year,discoverymethod+from+pscomppars&format=csv"
        response = requests.get(url)
        response.raise_for_status()
        data = pd.read_csv(StringIO(response.text), usecols=["pl_name", "hostname", "pl_orbper", "pl_rade", "pl_bmasse", "pl_eqt", "disc_year", "discoverymethod"])
        return data
    def analyze_planet(self, planet_name):
        planet_data = self.data[self.data['pl_name'] == planet_name]
        if planet_data.empty:
            print( f"No data available for {planet_name}.")
            return
        prompt = self._create_analysis_prompt(planet_data.iloc[0])
        response = self.client.chat.completions.create(model="llama-3.3-70b-versatile",messages=[
        {
        "role": "user",
        "content": prompt
        }],
        temperature=0.4)
        print(response.choices[0].message.content)
    def _create_analysis_prompt(self, planet_data):
        prompt = (f"""Provide a thorough scientific summary of the planet {planet_data['pl_name']} , Use these characteristics to help create the summary:
                  Temperature: {planet_data['pl_eqt']},
                  Orbital Period: {planet_data['pl_orbper']} days, 
                  Radius: {planet_data['pl_rade']} Earth radii, 
                  Mass: {planet_data['pl_bmasse']} Earth masses, 
                  Host Star: {planet_data['hostname']}, 
                  Discovery Method: {planet_data['discoverymethod']}.
                  Discovery Year: {planet_data['disc_year']}, """)
        return prompt
    def compare_planets(self, planet_names):
        planets_data = self.data[self.data['pl_name'].isin(planet_names)]
        if planets_data.empty:
            return "No data available for the specified planets."
        comparisons = []
        for _, row in planets_data.iterrows():
            comparisons.append(self._create_analysis_prompt(row))
        prompt = "Compare the following planets based on their respective summaries and characteristics: " + " ".join(comparisons)
        response = self.client.chat.completions.create(model="llama-3.3-70b-versatile",messages=[
        {
        "role": "user",
        "content": prompt
        }],
        temperature=0.2)
        print(response.choices[0].message.content)