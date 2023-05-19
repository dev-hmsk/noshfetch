import csv
import requests
import pandas as pd
import os

# Yelp API settings
YELP_API_KEY = os.environ.get('YELP_API_KEY')
YELP_API_URL = 'https://api.yelp.com/v3/businesses/search'

def search_yelp_api(api_key, location):
    # Set request headers
    headers = {
        'Authorization': f'Bearer {api_key}'
    }

    # Set request parameters
    params = {
        'term': 'restaurants',
        'location': location
    }

    # Send GET request to Yelp API
    response = requests.get(YELP_API_URL, headers=headers, params=params)
    data = response.json()
    print(data)
    # Extract restaurant data from the response
    restaurant_data = []
    for business in data['businesses']:
            name = business['name']
            address = ', '.join(business['location']['display_address'])
            rating = business['rating']
            phone = business['phone'] if 'phone' in business else ''
            website = business['url']
            cuisine = ', '.join(business['categories'][0]['title'].split(' & '))
            email = business['email'] if 'email' in business else ''
            restaurant_data.append([name, address, rating,
                                    phone, website, cuisine, email])

    return restaurant_data

def export_to_csv(data, filename):
    # Open the CSV file in write mode
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header row
        writer.writerow(['Name', 'Address', 'Rating',
                         'Phone', 'Website', 'Cuisine', 'Email'])
        
        # Write each restaurant's data as a row
        writer.writerows(data)
        
    print(f'Restaurant data exported to {filename} successfully!')

def import_csv_to_excel(csv_file, excel_file):
    # Read the CSV file using pandas
    df = pd.read_csv(csv_file)
    
    # Create an Excel writer using pandas
    writer = pd.ExcelWriter(excel_file)
    
    # Write the DataFrame to the Excel file
    df.to_excel(writer, index=False)
    
    # Save the Excel file
    writer._save()
    
    print(f'CSV file imported to Excel file {excel_file} successfully!')

# Yelp API key
api_key = YELP_API_KEY

# Location to search for restaurants (ZIP code or state)
location = input('Enter the location (ZIP code or state): ')

# Search Yelp API for restaurant data
data = search_yelp_api(api_key, location)

# Export the data to a CSV file
filename = 'restaurant_data.csv'
export_to_csv(data, filename)

# Import the CSV file into an Excel file
excel_file = 'restaurant_data.xlsx'
import_csv_to_excel(filename, excel_file)