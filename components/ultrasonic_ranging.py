#!/usr/bin/env python3
########################################################################
# Filename    : UltrasonicRanging.py
# Description : Get distance from UltrasonicRanging.
# Author      : freenove
# modification: 2018/08/03
########################################################################
import RPi.GPIO as GPIO
import time

trigPin = 16
echoPin = 18
MAX_DISTANCE = 220          #define the maximum measured distance
timeOut = MAX_DISTANCE*60   #calculate timeout according to the maximum measured distance

def pulseIn(pin,level,timeOut): # function pulseIn: obtain pulse time of a pin
    t0 = time.time()
    while(GPIO.input(pin) != level):
        if((time.time() - t0) > timeOut*0.000001):
            return 0;
    t0 = time.time()
    while(GPIO.input(pin) == level):
        if((time.time() - t0) > timeOut*0.000001):
            return 0;
    pulseTime = (time.time() - t0)*1000000
    return pulseTime

def getSonar():     #get the measurement results of ultrasonic module,with unit: cm
    GPIO.output(trigPin,GPIO.HIGH)      #make trigPin send 10us high level
    time.sleep(0.00001)     #10us
    GPIO.output(trigPin,GPIO.LOW)
    pingTime = pulseIn(echoPin,GPIO.HIGH,timeOut)   #read plus time of echoPin
    distance = pingTime * 340.0 / 2.0 / 10000.0     # the sound speed is 340m/s, and calculate distance
    return distance

def setup():
    GPIO.setmode(GPIO.BOARD)       #numbers GPIOs by physical location
    GPIO.setup(trigPin, GPIO.OUT)   #
    GPIO.setup(echoPin, GPIO.IN)    #

def loop():
    GPIO.setup(11,GPIO.IN)
    while(True):
        distance = getSonar()
        print ("The distance is : %.2f cm"%(distance))
        time.sleep(1)

if __name__ == '__main__':     #program start from here
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  #when 'Ctrl+C' is pressed, the program will exit
        GPIO.cleanup()         #release resource

# CUSTOM AREA
# -----------

def loop_during(looptime, interval=1):
    """ Get sonar value during some time

    - `time` is exprimed in seconds
    - `interval` is interval between each values exprimed in seconds
    """
    setup()
    GPIO.setup(11,GPIO.IN)
    while(looptime > 0):
        yield getSonar()
        looptime = looptime - interval
        time.sleep(interval)
    GPIO.cleanup()

def get_distance():
    """ Get sonar distance now
    """
    setup()
    GPIO.setup(11,GPIO.IN)
    distance = getSonar()
    GPIO.cleanup()
    return distance
