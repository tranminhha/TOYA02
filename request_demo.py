import requests
import os
import json
from dotenv import load_dotenv


resources_dir = 'D:/Python for DevOps/Mycode_python/week-4'
week_4_path = 'D:/Python for DevOps/Mycode_python/week-4'
google_map_api_url = 'https://maps.googleapis.com/maps/api/geocode/json'

load_dotenv(f'{week_4_path}/.env')
print(os.getenv('GOOGLE_MAPS_API_KEY'))


#sử dụng thư viện Requests
params = {
    'key': os.getenv('GOOGLE_MAPS_API_KEY'),
   'latlng' : '10.807782373172634,106.71010976618052',
}

response = requests.get(url=google_map_api_url, params=params)
results = response.json()
print(results)




