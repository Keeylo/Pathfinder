
import requests

import json


# Set the API key
with open('api_key.txt', 'r') as f:
    API_KEY = f.read()


#print(API_KEY)

mapstring = ("https://maps.googleapis.com/maps/api/place/findplacefromtext/json?fields=formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry&input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&key={id}").format(id = API_KEY)
response = requests.get(mapstring)

data = response.json()

if response.status_code == 200:
  with open('tester.json', 'w') as f:
     json.dump(data, f)

else:
   print("failed")




