#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

try:
        text = raw_input('Was soll geschrieben werden: ')
        print("Now place your tag to write")
        reader.write(text)
        print("Written. Exiting.")
finally:
        GPIO.cleanup()
