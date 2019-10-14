import requests

url = "https://www.cl.cam.ac.uk/research/dtg/weather/weather-raw.csv"
response = requests.get(url)
print(response.text)
