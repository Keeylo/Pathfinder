import requests
import json


# Set the API key
with open('api_key.txt', 'r') as f:
    API_KEY = f.read()

def responseFeedback(response):
  if response.status_code == 200:
    data = response.json()
    return data
  else:
    errorMessage = {
      "error": "Failed to fetch data",
      "status_code": response.status_code,
      "response": response.text
    }
    return errorMessage

DEBUG = True
GET = 2

def responseEndpoint(VERB, endpoint):
  if VERB == GET:
    response = requests.get(endpoint)
  return responseFeedback(response)

endpoint = ("https://maps.googleapis.com/maps/api/place/findplacefromtext/json?fields=formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry&input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&key={id}").format(id = API_KEY)

responses = []

responses.append(responseEndpoint(GET, endpoint))

### Output Section
with open("output.json", "w") as output_file:
  json.dump(responses, output_file, indent=2)
  

  


