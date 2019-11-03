import requests
import csv
import pandas
import matplotlib.pyplot as plt
import os

from helper_functions import save_csv_from_url

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

from normalise_functions import normalize_sun
from normalise_functions import normalize_wind


df = normalize_sun(df)
df = normalize_wind(df)

df = df.resample('D')

print(df)
