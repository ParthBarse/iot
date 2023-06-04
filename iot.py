# Q1) Write a program using Arduino to control LED (One or more ON/OFF). Or Blinking.

import time
import RPi.GPIO as GPIO

TRUE=1
led1=20
led2=21
led3=22
led4=23
led5=24
led6=25
led7=26
led8=27

my_led=[led1,led2,led3,led4,led5,led6,led7,led8]
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
GPIO.setup(led3,GPIO.OUT)
GPIO.setup(led4,GPIO.OUT)
GPIO.setup(led5,GPIO.OUT)
GPIO.setup(led6,GPIO.OUT)
GPIO.setup(led7,GPIO.OUT)
GPIO.setup(led8,GPIO.OUT)

def ledstate(led,a):
    GPIO.output(my_led[led],a)
    
def off_all():
    for i in range (0,8):
        ledstate(i,1)
    
try:
    off_all()
    while TRUE:
        for i in range(0,8):
            off_all()    
            ledstate(i,1)
            time.sleep(1)
            ledstate(i,0)
            time.sleep(0.5)


except KeyboardInterrupt:
    RUNNING=False
    print('Quit')
    GPIO.cleanup()

