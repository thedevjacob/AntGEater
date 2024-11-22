import requests, json

output = open("courses.json", 'w')
response = requests.get("https://api.peterportal.org/rest/v0/grades/calculated")

json.dump(response.json(), output, indent = 4)