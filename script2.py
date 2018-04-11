import requests
import json
import time
import RPi.GPIO as GPIO
from gateopsbak import gate_open, gate_close
#from ledops import led_on, led_off

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

flag_gate = 0
flag_blinds = 0
flag_textsms = 0
flag_water = 0

def led_on():
#    GPIO.setup(19, GPIO.OUT)
    GPIO.output(19, GPIO.HIGH)

def led_off():
#    GPIO.setup(19,GPIO.OUT)
    GPIO.output(19, GPIO.LOW)


def make_request(tag):
    global flag_textsms 
    url_link = "https://dweet.io/get/latest/dweet/for/{}".format(tag)
    r = requests.get(url_link)
    output = json.loads(r.content)
    if tag == 'nova_textsms':
        msg = output['with'][0]['content']['content'].split()
        for i in range(len(msg)):
            if 'approx' not in msg:
                return
            if msg[i] == 'approx':
                delay = int(msg[i+1])
                flag_textsms = 1
                # change control flag of gate (open gate)
                print "Delay : ",delay
                return delay
    return output['with'][0]['content']['status']

def gate_execute(input_flag):
    global flag_gate
    if flag_gate == input_flag:
        return
    if input_flag == 0:
        print 'Gate closed'
        gate_close()
        flag_gate = 0
    else:
        print 'Gate opened'
        gate_open()
        flag_gate = 1
       
        
def blinder_execute(input_flag):
    global flag_binds
    if flag_blinds == input_flag:
        return
    if input_flag == 0:
        print 'Close complete'
    elif input_flag == 1:
        print 'Open complete'
    else:
        print 'halfway'

def textsms_execute(delay):
    global textsms
    if flag_gate == 1:
        return
    if flag_textsms == 1:
        print ""
        time.sleep(delay)
        gate_open()
        flag_textsms = 0
        
def water_execute(input_flag):
    global flag_water
    if input_flag == flag_water:
        return
    if input_flag == 0:
        print "Springler Off"
        led_off()
        flag_water = 0
    else:
        print "Springler On"
        led_on()
        flag_water = 1
    
while True:
       p = make_request('nova_gate')
       print "GATE STATUS ",p
       gate_execute(p)
       q = make_request('nova_blinds')
       print "BLINDS STATUS ",q
       blinder_execute(q)
       make_request('nova_textsms')
       b = make_request('nova_water')
       print "Sprinkler", b
       water_execute(b)
       time.sleep(0.05)
       
        

