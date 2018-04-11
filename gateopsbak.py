import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

def gate_open():
    p = GPIO.PWM(16, 50)
    p.start(7.5)
    p.ChangeDutyCycle(7.5) 
    time.sleep(1) 
    p.ChangeDutyCycle(2.5)  
    time.sleep(1)
    p.stop()
#    GPIO.cleanup()
    
def gate_close():
    p = GPIO.PWM(16, 50)
    p.start(2.5)
    p.ChangeDutyCycle(2.5) 
    time.sleep(1) 
    p.ChangeDutyCycle(7.5)  
    time.sleep(1)
    p.stop()
#    GPIO.cleanup()
