import RPi.GPIO as GPIO
import requests
import json
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
pwm=GPIO.PWM(07, 100)

flag_open = False
flag_close = False

def blinds_stop():
	pwm=GPIO.PWM(07, 100)
	GPIO.output(07, GPIO.LOW)
	GPIO.output(12, GPIO.LOW)
	GPIO.output(11, GPIO.LOW)
	pwm.stop()

def blinds_open():
	global flag_open
	if not flag_open:
		pwm.ChangeDutyCycle(50)
		GPIO.output(7, GPIO.HIGH)
		GPIO.output(12, GPIO.LOW)
		GPIO.output(11, GPIO.HIGH)
		print "Blinds Open"

def blinds_close():
#	global flag_close
	if not flag_close:
		pwm.ChangeDutyCycle(50)
		GPIO.output(7, GPIO.HIGH)
		GPIO.output(12, GPIO.HIGH)
		GPIO.output(11, GPIO.LOW)
		print "Blinds Close"


url = "https://dweet.io/get/latest/dweet/for/nova_blinds"

def get_status():
        r = requests.get(url)
        output = json.loads(r.content)
        if output['this'] == 'failed':
                return 'failed'
        return output['with'][0]['content']['status']

while True:
	global flag_close
	global flag_open
        status = get_status()
	print status
        if status == 'failed':
                print "No request"
                continue
        if status == 0:
#		blinds_stop()
		blinds_close()
		time.sleep(2)
		blinds_stop()
		flag_close = True
		flag_open = False
#                print "Blinds Close"

        elif status == 1:
#                blinds_stop()
                blinds_open()
                time.sleep(2)
                blinds_stop()
		flag_open = True
		flag_close = False
 #               print "Blinds Open"
	else:
#		blinds_stop()
		blinds_open()
		time.sleep(1)
		blinds_stop()
		flag_open = False
		flag_close = False
		print "Blinds open halfway"

        time.sleep(0.5)
