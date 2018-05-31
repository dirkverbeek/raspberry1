## Web-controlled LED

import RPi.GPIO as GPIO
import time
import sys
from pubnub import Pubnub
GPIO.setmode (GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)

pubnub = Pubnub(publish_key='pub-c-9e2fd6cb-ef65-42c7-9707-87f997023175', subscribe_key='sub-c-0ebf3c70-c03d-11e5-8a35-0619f8945a4f')
channel = 'led'

def _callback(message, channel):
	if message['led'] == 1:
			GPIO.output(18,1)
	elif message['led'] == 0:	
			GPIO.output(18,0)
	elif message['led'] == 2:	
			GPIO.output(17,0)
	elif message['led'] == 3:	
			GPIO.output(17,1)

def _error(message):
	print(message)
pubnub.subscribe(channels=channel, callback=_callback, error=_error)
