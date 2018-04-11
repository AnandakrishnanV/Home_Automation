
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT) 
GPIO.setup(11, GPIO.OUT) 
GPIO.setup(12, GPIO.OUT)

pwm=GPIO.PWM(07, 100)

pwm.ChangeDutyCycle(50)

GPIO.output(7, GPIO.HIGH)

GPIO.output(12, GPIO.LOW)
GPIO.output(11, GPIO.HIGH)
