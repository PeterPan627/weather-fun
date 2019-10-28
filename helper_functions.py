import urllib

def save_csv_from_url(url, saving_path):
	""" Downloads data from a url and saves it to a specified path. """
	response = urllib.request.urlopen(url)
	with open(saving_path, 'wb') as f:
		f.write(response.read())
