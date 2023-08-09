# API Data Exporter 
This document provides information about two Python scripts that utilize APIs to search for businesses in a specified location and export their information to CSV files.

### Table of Contents
- Yelp API Restaurant Data Exporter
- Google Places API Business Data Exporter

### Yelp API Restaurant Data Exporter
#### Requirements
- Python 3.x
- Yelp API Key (set as an environment variable named YELP_API_KEY)

#### Installation
1. Clone the repository to your local machine.
2. Set up the Yelp API Key: Set your Yelp API key as an environment variable named YELP_API_KEY.

#### Usage
- Run the script: Navigate to the repository directory and execute the script using `python script.py`.
- Enter the location: When prompted, enter the location you want to search for (ZIP code or state).
- Data Export: The script will use the Yelp API to fetch restaurant data
- It will then export it to both a CSV file (restaurant_data.csv) and an Excel file (restaurant_data.xlsx).

#### Customization
- Modify the parameters in the search_yelp_api function to refine your search (e.g., change the term to search for other businesses, adjust the location).
- Customize the column headers and data fields in the exported CSV and Excel files by modifying the respective functions.

### Google Places API Business Data Exporter

#### Requirements
- Python 3.x
- Google API Key (set as an environment variable named GOOGLE_API_KEY)

#### Installation
1. Clone the repository to your local machine.
2. Set up the Google API Key: Set your Google API key as an environment variable named GOOGLE_API_KEY.

#### Usage
- Run the script: Navigate to the repository directory and execute the script using python google_api.py.
- Enter the location: When prompted, enter the location you want to search for.
- Data Export: The script will use the Google Places API to fetch business data and export it to a CSV file (businesses.csv).

#### Customization
- Modify the search_google_api function to adjust the search parameters (e.g., change the keyword, location).
- Customize the column headers and data fields in the exported CSV file by modifying the save_to_csv function.

#### License
These projects are licensed under the MIT License.

