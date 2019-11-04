import urllib
from suntime import Sun
import pandas
import numpy as np
import os

def save_csv_from_url(url, saving_path):
	""" Downloads data from a url and saves it to a specified path. """
	response = urllib.request.urlopen(url)
	with open(saving_path, 'wb') as f:
		f.write(response.read())

def sunshine_hours(date_time):
	''' calculates total seconds of daylight for a given day'''
	CAMBRIDGE_LAT = 52.2053
	CAMBRIDGE_LON = 0.1218
	sun_obj = Sun(CAMBRIDGE_LAT, CAMBRIDGE_LON)
	sunrise = sun_obj.get_sunrise_time(date_time)
	sunset = sun_obj.get_sunset_time(date_time)
	return (sunset - sunrise).seconds/3600

def fix_units(df):
	''' Fixes the units in the raw dataset '''

	df['Temperature'] = df['Temperature'].apply(lambda x: x/10)
	df['DewPoint'] = df['DewPoint'].apply(lambda x: x/10)
	df['MeanWindSpeed'] = df['MeanWindSpeed'].apply(lambda x: x/10)
	df['Sunshine'] = df['Sunshine'].apply(lambda x: x/100)
	df['Rainfall'] = df['Rainfall'].apply(lambda x: x/1000)
	df['MaxWindSpeed'] = df['MaxWindSpeed'].apply(lambda x: x/10)

def normalise_sun(df):
	''' Normalise sunshine time by daylight length'''

	df['sun_rise_set'] = df.index.to_series().apply(sunshine_hours)
	df['Sunshine'] = df['Sunshine']/df['sun_rise_set']
	df.drop(['sun_rise_set'], axis = 1, inplace = True)

def import_data():
	''' Import the dataset'''

	url = "https://www.cl.cam.ac.uk/research/dtg/weather/weather-raw.csv"
	data_file = "data.csv"
    # Only download CSV if not present locally
	if not os.path.exists(data_file):
		save_csv_from_url(url, data_file)
	headers = ["Timestamp","Temperature","Humidity","DewPoint","Pressure",
            "MeanWindSpeed","WindBearing","Sunshine","Rainfall","MaxWindSpeed"]
	df = pandas.read_csv(data_file, names=headers)
	df['Timestamp'] = pandas.to_datetime(df['Timestamp'])
	df['Temperature'] = pandas.to_numeric(df['Temperature'])
	df = df.set_index('Timestamp')
	df = df.resample('D').agg({'Temperature': np.mean,
                                'Humidity': np.mean,
                                'DewPoint': np.mean,
                                'Pressure': np.mean,
                                'MeanWindSpeed': np.mean,
                                'WindBearing': np.mean,
                                'Sunshine': np.sum,
                                'Rainfall': np.sum,
                                'MaxWindSpeed': np.max
                                })
	return df
