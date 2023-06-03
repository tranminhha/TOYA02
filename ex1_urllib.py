

import requests
import os
import json
from dotenv import load_dotenv

import urllib.parse
import urllib.request

resources_dir = 'D:/Python for DevOps/Mycode_python/week-4'
week_4_path = 'D:/Python for DevOps/Mycode_python/week-4'
google_map_api_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

load_dotenv(f'{week_4_path}/.env')
print(os.getenv('GOOGLE_MAPS_API_KEY'))


params = dict(
latlng='10.807782373172634,106.71010976618052',
)

url = google_map_api_url + urllib.parse.urlencode(params) 
resp = urllib.request.urlopen(url) 
data = resp.read() 
js = json.loads(data) 

print(js)