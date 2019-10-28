import requests
import csv
import pandas
import os

from helper_functions import save_csv_from_url

url = "https://www.cl.cam.ac.uk/research/dtg/weather/weather-raw.csv"
data_file = "data.csv"

if not os.path.exists(data_file):
	save_csv_from_url(url, data_file)

headers = ["Timestamp","Temperature","Humidity","DewPoint","Pressure",
		   "MeanWindSpeed","WindBearing","Sunshine","Rainfall","MaxWindSpeed"]

df = pandas.read_csv(data_file, names=headers)

print(df)
