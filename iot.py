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

# Q2) Create a program so that when the user enters ‘b’ the green light blinks, ‘g’ thegreen light is illuminated ‘y’ the yellow light is illuminated and ‘r’ the red light is illuminated.

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
        inp = input("Enter your Choice : ")
        if inp == "y":
            off_all()
            GPIO.output(led1, 0)
            GPIO.output(led2, 0)

        elif inp == "g":
            off_all()
            GPIO.output(led3, 0)
            GPIO.output(led4, 0)

        elif inp == "r":
            off_all()
            GPIO.output(led5, 0)
            GPIO.output(led6, 0)

        else:
            print('Invalid Input')
            off_all()

except KeyboardInterrupt:
    RUNNING=False
    print('Quit')
    GPIO.cleanup()

# Q3) Write a program that asks the user for a number and outputs the number squared that is entered.

a = int(input("Enter the number = "))
n = a**(1/2)
print("The square root of the number is : ",n)

# Q4) Write a program read the temperature sensor and send the values to the serial monitor on the computer

import time
import os

base_dir="/sys/bus/w1/devices/28-000008bdd91e/w1_slave"

def read_temp_raw():
    f = open(base_dir, "r")
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    
    while lines[0].strip()[-3:] ==  "YES":
        time.sleep(1)
        lines = read_temp_raw()
        equal_pos = lines[1].find("t=")
        
        if equal_pos != -1:
            temp_string=lines[1][equal_pos+2:]
            temp_c=float(temp_string)/1000
            return temp_c
        
while True:
    print(read_temp())
    break
    
# Q5) Write a program so it displays the temperature in Fahrenheit as well as the maximum and minimum temperatures it has seen.


import time
import os

base_dir="/sys/bus/w1/devices/28-000008bdd91e/w1_slave"

def read_temp_raw():
    f = open(base_dir, "r")
    lines = f.readlines()
    f.close()
    return lines

temp=[]

def read_temp():
    lines = read_temp_raw()
    
    while lines[0].strip()[-3:] ==  "YES":
        time.sleep(1)
        lines = read_temp_raw()
        equal_pos = lines[1].find("t=")
        
        if equal_pos != -1:
            temp_string=lines[1][equal_pos+2:]
            temp_c=float(temp_string)/1000
            temp_f=temp_c*(9.0/5.0)+32.0
            temp.append(temp_f)
            return(temp_f)

try:    
    while True:
        print(read_temp())

except KeyboardInterrupt:
        max=temp[0]
        min=temp[0]
        print('Readings: ',temp)
        for i in (temp):
            if(i>max):
                max=i
        for i in (temp):
            if(i<min):
                min=i
        print('min: ',min)
        print('max: ',max)
            
# Q6) Write a program to show the temperature and shows a graph of the recent measurements.

import matplotlib.pyplot as plt
import time
import os

base_dir="/sys/bus/w1/devices/28-000008bdd91e/w1_slave"

def read_temp_raw():
    f = open(base_dir, "r")
    lines = f.readlines()
    f.close()
    return lines

temp=[]

try:

    def graph(temp):
        x=[]
        for i in range(len(temp)):
            x.append(i)
        y=temp
        plt.plot(x,y)
        plt.show()
            
    def min_max(temp):
        max=temp[0]
        min=temp[0]
        print('Readings: ',temp)
        for i in (temp):
            if(i>max):
                max=i
        for i in (temp):
            if(i<min):
                min=i
        print('min: ',min)
        print('max: ',max)


    def read_temp():
        lines = read_temp_raw()
        
        while lines[0].strip()[-3:] ==  "YES":
            time.sleep(1)
            lines = read_temp_raw()
            equal_pos = lines[1].find("t=")
            
            if equal_pos != -1:
                temp_string=lines[1][equal_pos+2:]
                temp_c=float(temp_string)/1000
                temp.append(temp_c)
                return(temp_c)
        
        
    while True:
            print(read_temp())
            graph(temp)
except:
    min_max(temp)

# Q7) Write a program using piezo element and use it to play a tune after someone knocks

import time
import RPi.GPIO as GPIO

RUNNING = True

HIGH = 1
LOW = 0
DetectPin = 5
Buzzer = 3
RUNNING = True

def InitSystem():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Buzzer, GPIO.OUT)
    GPIO.setup(DetectPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    return

def DetectPerson():
    while True:
        input_state = GPIO.input(DetectPin)
        time.sleep(0.3)
        if input_state == 0:
            return LOW
        else:  
            return HIGH

def BuzzerRing(val):
    GPIO.output(Buzzer, val)
              
try:
    print("Input using IR LED")
    print("---------------------------------")
    InitSystem()
    count = 0
    while RUNNING:
        state = DetectPerson()
        if state == HIGH:
            BuzzerRing(1)
            time.sleep(1)
            BuzzerRing(0)
            time.sleep(1)
            print("Knock Count = ",count)
            
except KeyboardInterrupt:
    RUNNING = False
    print("Stopping")
    
finally:
    GPIO.cleanup()


# Q8) Understanding the connectivity of Raspberry-Pi /Beagle board circuit / Arduino with IR Sensor . Write an Application to detect obstacle and notify user using LED’s.

import time
import RPi.GPIO as GPIO

RUNNING = True

HIGH = 1
LOW = 0
DetectPin = 5

led1=20

def InitSystem():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led1,GPIO.OUT)
    GPIO.setup(DetectPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    return

def DetectPerson():
    while True:
        input_state = GPIO.input(DetectPin)
        time.sleep(0.3)
        if input_state == 0:
            return LOW
        else:   
            return HIGH
              
try:
    print("Reading using IR LED")
    print("---------------------------------")
    InitSystem()
    count = 0
    while RUNNING:
        GPIO.output(led1,1)
        state = DetectPerson()
        if state == HIGH:
            GPIO.output(led1,0)
            count+=1
            print("Obstracle count = ",count)
            
except KeyboardInterrupt:
    RUNNING = False
    print("Stopping")
    
finally:
    GPIO.cleanup()

# Q9) Write a program using Arduino (Used Raspberrypi) to control LED alternate Blinking of LED.

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

# Q10) Create a program so that when the user enters ‘b’ two LEDs will blink, ‘g’ the is next two LEDs will illuminate and ‘y’ the four Led will illuminated.

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
        inp = input("Enter your Choice : ")
        if inp == "b":
            off_all()
            GPIO.output(led1, 0)
            GPIO.output(led2, 0)

        elif inp == "g":
            off_all()
            GPIO.output(led3, 0)
            GPIO.output(led4, 0)

        elif inp == "y":
            off_all()
            GPIO.output(led1, 0)
            GPIO.output(led2, 0)
            GPIO.output(led3, 0)
            GPIO.output(led4, 0)

        else:
            print('Invalid Input')
            off_all()

except KeyboardInterrupt:
    RUNNING=False
    print('Quit')
    GPIO.cleanup()

# Q11) Write a program read the temperature sensor and send the values to the serial monitor on the computer

import time
import os

base_dir="/sys/bus/w1/devices/28-000008bdd91e/w1_slave"

def read_temp_raw():
    f = open(base_dir, "r")
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    
    while lines[0].strip()[-3:] ==  "YES":
        time.sleep(1)
        lines = read_temp_raw()
        equal_pos = lines[1].find("t=")
        
        if equal_pos != -1:
            temp_string=lines[1][equal_pos+2:]
            temp_c=float(temp_string)/1000
            return temp_c
        
while True:
    print(read_temp())
    break

# Q12) Write a program so it displays the temperature in Celsius as well as the maximum and minimum temperatures it has seen

import time
import os

base_dir="/sys/bus/w1/devices/28-000008bdd91e/w1_slave"

def read_temp_raw():
    f = open(base_dir, "r")
    lines = f.readlines()
    f.close()
    return lines

temp=[]

def read_temp():
    lines = read_temp_raw()
    
    while lines[0].strip()[-3:] ==  "YES":
        time.sleep(1)
        lines = read_temp_raw()
        equal_pos = lines[1].find("t=")
        
        if equal_pos != -1:
            temp_string=lines[1][equal_pos+2:]
            temp_c=float(temp_string)/1000
            temp.append(temp_c)
            return(temp_c)

try:    
    while True:
        print(read_temp())

except KeyboardInterrupt:
        max=temp[0]
        min=temp[0]
        print('Readings: ',temp)
        for i in (temp):
            if(i>max):
                max=i
        for i in (temp):
            if(i<min):
                min=i
        print('min: ',min)
        print('max: ',max)

# Q13) Write a program using piezo element and use it to play a buzzer after someone knocks

import time
import RPi.GPIO as GPIO

RUNNING = True

HIGH = 1
LOW = 0
DetectPin = 5
Buzzer = 3
RUNNING = True

def InitSystem():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Buzzer, GPIO.OUT)
    GPIO.setup(DetectPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    return

def DetectPerson():
    while True:
        input_state = GPIO.input(DetectPin)
        time.sleep(0.3)
        if input_state == 0:
            return LOW
        else:  
            return HIGH

def BuzzerRing(val):
    GPIO.output(Buzzer, val)
              
try:
    print("Input using IR LED")
    print("---------------------------------")
    InitSystem()
    count = 0
    while RUNNING:
        state = DetectPerson()
        if state == HIGH:
            BuzzerRing(1)
            time.sleep(1)
            BuzzerRing(0)
            time.sleep(1)
            print("Knock Count = ",count)
            
except KeyboardInterrupt:
    RUNNING = False
    print("Stopping")
    
finally:
    GPIO.cleanup()


# Q14) Write an application to detect obstacle and notify user using LEDs using IR sensor

import time
import RPi.GPIO as GPIO

RUNNING = True

HIGH = 1
LOW = 0
DetectPin = 5

led1=20

def InitSystem():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led1,GPIO.OUT)
    GPIO.setup(DetectPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    return

def DetectPerson():
    while True:
        input_state = GPIO.input(DetectPin)
        time.sleep(0.3)
        if input_state == 0:
            return LOW
        else:   
            return HIGH
              
try:
    print("Reading using IR LED")
    print("---------------------------------")
    InitSystem()
    count = 0
    while RUNNING:
        GPIO.output(led1,1)
        state = DetectPerson()
        if state == HIGH:
            GPIO.output(led1,0)
            count+=1
            print("Obstracle count = ",count)
            
except KeyboardInterrupt:
    RUNNING = False
    print("Stopping")
    
finally:
    GPIO.cleanup()