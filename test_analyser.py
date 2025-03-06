from exoplanet import *

def display_menu():
    print("\nWelcome To Exoplanet Analyzer")
    print("1. Analyze a planet")
    print("2. Compare different planets")
    print("3. End Session")

analyzer = ExoplanetAnalyzer()
while True:
    display_menu()

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        planet_name = input("Please enter the name of the exoplanet to be analyzed: ")
        analyzer.analyze_planet(planet_name)
    elif choice == "2":
        planet_names = input("Please enter the names of exoplanets you want to compare, make sure there is a comma separating them(,): ")
        planet_names = [name.strip() for name in planet_names.split(",")]
        analyzer.compare_planets(planet_names)
    elif choice == "3":
        print("Exiting the Exoplanet Analyzer.")
        break
    else:
        print("Invalid choice, Try again.")