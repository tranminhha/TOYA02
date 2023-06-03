import http.client
import json
import os
from dotenv import load_dotenv

resources_dir = 'D:/Python for DevOps/Mycode_python/week-4'
week_4_path = 'D:/Python for DevOps/Mycode_python/week-4'
google_map_api_url = 'https://maps.googleapis.com/maps/api/geocode/json'

load_dotenv(f'{week_4_path}/.env')
print(os.getenv('GOOGLE_MAPS_API_KEY'))

connect = http.client.HTTPConnection("maps.googleapis.com") 
params = "latlng=10.807782373172634,106.71010976618052" 
connect.request("GET", "/maps/api/geocode/json?" + params) 

resp = connect.getresponse() 
data = resp.read() 

js = json.loads(data) 
print(js)


