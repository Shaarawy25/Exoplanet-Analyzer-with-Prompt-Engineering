# Exoplanet Analyzer

## Overview
Exoplanet Analyzer is a Python-based tool that retrieves, analyzes, and compares exoplanetary data from the NASA Exoplanet Archive. It leverages OpenAI's language model to generate detailed scientific summaries of exoplanets based on their properties.

## Features
- **Analyze a specific exoplanet**: Retrieve and summarize key details such as orbital period, radius, mass, temperature, and discovery method.
- **Compare multiple exoplanets**: Generate comparative insights between selected exoplanets.
- **Fetch real-time data**: Retrieves the latest exoplanetary data directly from NASA's Exoplanet Archive.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Required libraries: `requests`, `pandas`, `openai`, `dotenv`

### Setup
1. **Clone the Repository**:
   ```sh
   git clone https://github.com/your-username/exoplanet-analyzer.git
   cd exoplanet-analyzer
   ```

2. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Create a `.env` file in the project root directory.
   - Add your Groq API key:
     ```sh
     GROQ_API_KEY=your_api_key_here
     ```

## Usage
### Running the Program
Execute the following command in the terminal:
```sh
python main.py
```

### Menu Options
1. **Analyze a planet**: Enter the name of a known exoplanet to retrieve a scientific summary.
2. **Compare planets**: Provide a comma-separated list of exoplanet names to compare their characteristics.
3. **Exit the program**: Safely close the application.

## Project Structure
```
📂 exoplanet-analyzer
│── 📄 exoplanet.py    # Exoplanet analysis module
│── 📄 main.py         # Main program interface
│── 📄 .env.example    # Example environment file
│── 📄 requirements.txt # Dependencies list
│── 📄 README.md       # Project documentation
```

## Notes
- Ensure your internet connection is active to fetch exoplanet data.
- The OpenAI API requires a valid API key for requests.

## License
This project is licensed under the MIT License.

