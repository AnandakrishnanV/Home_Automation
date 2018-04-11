import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT) 
GPIO.setup(11, GPIO.OUT) 
GPIO.setup(12, GPIO.OUT)

pwm=GPIO.PWM(07, 100)

GPIO.output(07, GPIO.LOW)

GPIO.output(12, GPIO.LOW) 
GPIO.output(11, GPIO.LOW)
pwm.stop()
