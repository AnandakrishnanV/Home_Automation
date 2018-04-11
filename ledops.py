import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
def led_on():
    GPIO.setup(19, GPIO.OUT)
    GPIO.output(19, GPIO.HIGH)

def led_off():
    GPIO.setup(19,GPIO.OUT)
    GPIO.output(19, GPIO.LOW)
