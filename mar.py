import requests

def query(addr):
	r = requests.post(
			'http://citizenatlas.dc.gov/newwebservices/locationverifier.asmx/findLocation2',
			data={'f': 'json', 'str': addr})
	r.raise_for_status()
	return r.json

if __name__ == "__main__":
	import sys, json
	if len(sys.argv) < 2:
		print("Usage: python mar.py \"3460 14th St NW #125\"")
		sys.exit(1)
	print(json.dumps(query(sys.argv[1]), indent=2, sort_keys=True))
