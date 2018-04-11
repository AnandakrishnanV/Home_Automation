
def gate_open():
    GPIO.setup(16, GPIO.OUT)
    p = GPIO.PWM(16, 50)
    p.start(7.5)
    p.ChangeDutyCycle(7.5) 
    time.sleep(1) 
    p.ChangeDutyCycle(2.5)  
    time.sleep(1)
    p.stop()
    GPIO.cleanup()
    
def gate_close():
    GPIO.setup(16, GPIO.OUT)
    p = GPIO.PWM(16, 50)
    p.start(2.5)
    p.ChangeDutyCycle(2.5) 
    time.sleep(1) 
    p.ChangeDutyCycle(7.5)  
    time.sleep(1)
    p.stop()
    GPIO.cleanup()


    
    