import requests
import os

# NASA APOD API endpoint
api_url = "https://api.nasa.gov/planetary/apod"
public_apod_url = "https://apod.nasa.gov/apod/"


# API key
nasa_api_key = os.getenv("NASA_API_KEY")

# Make a GET request to the endpoint with the API key
response = requests.get(api_url + "?api_key=" + nasa_api_key)

# Check the status code of the response
if response.status_code == 200:
    # If the status code is 200 (OK), get the JSON data from the response
    data = response.json()

    # Print the title and explanation of the APOD
    apod_response = "Sure, here is a link to the Astronomy Picture of the Day, today's picture is of: {0} and you can see it at {1}".format(data["title"],public_apod_url)
    print(apod_response)

else:
    # If the status code is not 200 (OK), print an error message
    apod_err = "Sorry, I wasn't able to hit the NASA API at this time."
    print("An error occurred while fetching the data:", response.text)