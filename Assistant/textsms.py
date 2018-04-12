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


url = "https://dweet.io/get/latest/dweet/for/nova_textsms"

def get_status():
        r = requests.get(url)
        output = json.loads(r.content)
        if output['this'] == 'failed':
                return 'failed'
        msg = output['with'][0]['content']['content'].split()
        for i in range(len(msg)):
            if 'approx' not in msg:
                return 0
            if msg[i] == 'approx':
                delay = int(msg[i+1])
                flag_textsms = 1
                # change control flag of gate (open gate)
                print "Delay : ",delay
                return delay


while True:
        delay = get_status()
        if delay == 'failed':
                print "No request"
                continue
	elif delay == 0:
		continue
        else:
		time.sleep(delay)
		gate_open()
        time.sleep(0.2)

