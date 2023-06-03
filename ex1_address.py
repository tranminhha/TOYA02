
import requests
import os
import json
from dotenv import load_dotenv


resources_dir = 'D:/Python for DevOps/Mycode_python/week-4'
week_4_path = 'D:/Python for DevOps/Mycode_python/week-4'
google_map_api_url = 'https://maps.googleapis.com/maps/api/geocode/json'

load_dotenv(f'{week_4_path}/.env')
print(os.getenv('GOOGLE_MAPS_API_KEY'))

params = dict(
address='82/2/9 Đinh Bộ Lĩnh, phường 26, quận Bình Thạnh, TP.HCM',
sensor='false',
region='vn'
)

resp = requests.get(url=google_map_api_url, params=params)
data = resp.json() # Lấy dữ liệu JSON

print(data)