import requests
import json
import time
import RPi.GPIO as GPIO
from gateops import gate_open, gate_close

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)

flag_gate = 0
flag_blinds = 0
flag_textsms = 0

def make_request(tag):        
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
    if flag_gate == input_flag:
        return
    if input_flag == 0:
        print 'Gate closed'
        gate_close()
    else:
        print 'Gate opened'
        gate_open()
       
        
def blinder_execute(input_flag):
    if flag_binds == input_flag:
        return
    if input_flag == 0:
        print 'Close complete'
    elif input_flag == 1:
        print 'Open complete'
    else:
        print 'halfway'

def textsms_execute(delay):
    if flag_gate == 1:
        return
    if flag_textsms == 1:
        time.sleep(delay)
        flag_textsms = 0
    
while True:
       p = make_request('nova_gate')
       print "GATE STATUS ",
       print p
       gate_execute(p)
       q = make_request('nova_blinds')
       print "BLINDS STATUS ",
       print q
       q = make_request('nova_textsms')
       time.sleep(0.2)
        


