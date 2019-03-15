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
        # Ignore additional data on tag
        id, data = reader.read()
        print(f"Found student id: {id}")
        student_url = f"{url}/{id}"
        print(f"Fetching data from {student_url}...")
        response = requests.get(url=student_url)
        print(f"Received: {response}")
        print("Parsing data...")
        data = response.json()
        print("Found data...")
        print(data)
        # webbrowser.open_new_tab(student_url)

finally:
    GPIO.cleanup()
