import RPi.GPIO as GPIO
import requests
import json
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)

def gate_open():
	p = GPIO.PWM(16, 50)
	p.start(2.5)
	p.ChangeDutyCycle(2.5)
	time.sleep(1)
	p.stop()

def gate_off():
	p = GPIO.PWM(16, 50)
	p.start(7.5)
	p.ChangeDutyCycle(7.5)
	time.sleep(1)
	p.stop()


url = "https://dweet.io/get/latest/dweet/for/nova_gate"

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
                gate_open()
                print "Gate on"
        else:
                gate_off()
                print "Gate off"
        time.sleep(0.5)

