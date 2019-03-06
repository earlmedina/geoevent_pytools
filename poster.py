import json, requests, os
# URL: https://machine.domain.com:6143/geoevent/rest/receiver/rest-features-in
# Header: Content-Type: application/json

def poster_json(url):
	url = "https://machine.domain.com:6143/geoevent/rest/receiver/mysqltest"
	# Create a dictionary below holding the desired headers
	headers = {'Content-Type': 'application/json'}
	r = requests.post(url, data=json.dumps({"SITENAME":"MS_SUMMIT_800"}),headers=headers, verify=False)
	print(r.status_code,'\t',r.headers)

def poster():
	url = "https://machine.domain.com:6143/geoevent/rest/receiver/mysqltest"
	r = requests.post(url, json={"SITENAME":"MS_SUMMIT_800"},verify=False)
	print(r.status_code,'\t',r.headers)

def poster_file():
	# Read the json file (here named test2.json
	basedir = os.path.abspath(os.path.dirname(__file__))
	file = os.path.join(basedir,'test.json')

	with open(file) as json_data:
		test = json.load(json_data)
	url = "https://machine.domain.com:6143/geoevent/rest/receiver/mysqltest"
	r = requests.post(url, json=test,verify=False)
	print(r.status_code,'\t',r.headers)

poster_file()
