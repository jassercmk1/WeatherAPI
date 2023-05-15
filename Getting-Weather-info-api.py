import requests
from pprint import pprint


# Enter your API key here
api_key = "get your api key from this link = https://openweathermap.org/appid"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Get city name from user input
city_name = input("Enter city name: ")

# Create the complete URL for the API call
complete_url = f"{base_url}appid={api_key}&q={city_name}"

try:
    # Send the API request and store the response
    response = requests.get(complete_url)

    # Check if the API call was successful
    if response.status_code == 200:
        # Convert the JSON response to a Python dictionary
        data = response.json()
        # Print the response in a human-readable format
        pprint(data)
    else:
        print(f"Error: Unable to get weather data for {city_name}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")
