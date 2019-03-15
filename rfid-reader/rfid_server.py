#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import requests
# import webbrowser

reader = SimpleMFRC522.SimpleMFRC522()
url = 'https://my-json-server.typicode.com/kuehnert/msoportal/students'

try:
	while True:
		print("\n\nWaiting for scan")
		id = reader.read()
		print(f"Found student id: {id}")
		print("Fetching data...")
		response = requests.get(url=f"{url}/{id}")
		print("Parsing data...")
		data = response.json()
		print("Found data...")
		print(data)
		# webbrowser.open_new_tab(f"{url}/{id}")

finally:
    GPIO.cleanup()
