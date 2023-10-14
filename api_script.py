
import requests

# Set the API key
API_KEY = "YOUR_API_KEY"

# Make the request
response = requests.get("https://api.example.com/v1/users",
                        headers={"Authorization": "Bearer {}".format(API_KEY)})

# Check the response status code
if response.status_code == 200:
  # The request was successful
  # Do something with the response data
else:
  # The request failed
  # Handle the error
