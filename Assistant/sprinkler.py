import RPi.GPIO as GPIO
import requests
import json
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.OUT)

def sprinkler_on():
	GPIO.output(19, GPIO.HIGH)
def sprinkler_off():
	GPIO.output(19, GPIO.LOW)


url = "https://dweet.io/get/latest/dweet/for/nova_water"

def get_status():
	r = requests.get(url)
	output = json.loads(r.content)
	if output['this'] == 'failed':
		return 'failed'
	return output['with'][0]['content']['status']

while True:
	status = get_status()
	if status == 'failed':
		print "No request"
		continue
	if status == 1:
		sprinkler_on()
		print "Sprinkler on"
	else:
		sprinkler_off()
		print "Sprinkler off"
	time.sleep(0.2)

