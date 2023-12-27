import requests
from datetime import datetime
import time

LAT = 43.653225
LONG = -79.383186

PARAMS = {
  'lat': LAT,
  'lng': LONG,
  'formatted': 0
}

def get(url, params=None):

  resp = requests.get(url, params=params)
  resp.raise_for_status() 

  return resp.json()

s_data = get('https://api.sunrise-sunset.org/json', PARAMS)

sunset_resp = s_data['results']['sunset']
sunset_time = sunset_resp.split('T')[1]
sunset_hour = int(sunset_time.split(':')[0])

current_time = datetime.now()
current_hour = current_time.hour

is_night = current_hour >= sunset_hour
is_iss_above = False

if is_night:
    while not(is_iss_above):
        iss_data = get('http://api.open-notify.org/iss-now.json')
        iss_position = iss_data['iss_position']
        iss_lat, iss_long = float(iss_position['latitude']), float(iss_position['longitude'])
        is_iss_above = round((iss_lat - LAT), 0) == 0 and round((iss_long - LONG), 0) == 0
        time.sleep(60)
        print('Not yet')

    print('Look up!')
