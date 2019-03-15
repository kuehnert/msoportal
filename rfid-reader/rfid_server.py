#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import requests
# import webbrowser

reader = SimpleMFRC522.SimpleMFRC522()
url = 'https://my-json-server.typicode.com/kuehnert/msoportal/students/'

try:
	while True:
		id = reader.read()
		print("Found student id: " + id)
		print("Fetching data...")
		response = requests.get(url=url)
		print("Parsing data...")
		data = response.json()
		print("Found data...")
		print(data)
		# webbrowser.open_new_tab(url + id)

finally:
    GPIO.cleanup()
