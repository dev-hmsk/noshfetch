import requests
import os
import csv

GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
GOOGLE_API_URL = 'https://maps.googleapis.com/maps/api/place/textsearch/json'

def search_google_api(api_key, location, keyword):
    # Set request parameters
    params = {
        'key': api_key,
        'query': keyword,
        'location': location
    }

    # Send GET request to Google Places API
    response = requests.get(GOOGLE_API_URL, params=params)
    data = response.json()

    # Extract business data from the response
    business_data = []
    for result in data['results']:
        name = result['name']
        address = result['formatted_address']
        rating = result.get('rating', '')
        phone = result.get('formatted_phone_number', '')
        website = result.get('website', '')
        business_data.append([name, address, rating, phone, website])
    return business_data

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Address', 'Rating', 'Phone', 'Website'])
        writer.writerows(data)

# Set your location
location = input("Enter a location: ")

# Search for businesses with a specific keyword
keyword = 'restaurants'
business_data = search_google_api(GOOGLE_API_KEY, location, keyword)

# Save the data to a CSV file
filename = 'businesses.csv'
save_to_csv(business_data, filename)
