#!/usr/bin/python3

import time
import motor as move
import RPi.GPIO as GPIO
import argparse
Tr = 11#trigger pin
Ec = 8#echo pin

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Tr, GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(Ec, GPIO.IN)



def checkdist(exact=False):       #Reading distance
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Tr, GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(Ec, GPIO.IN)
    GPIO.output(Tr, GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(Tr, GPIO.LOW)
    while not GPIO.input(Ec):
        pass
    t1 = time.time()
    while GPIO.input(Ec):
        pass
    t2 = time.time()
    if exact == False:
        return round((t2-t1)*340/2,2)
    
    elif exact != False:
       return (t2-t1)*340/2 #  gives the answers in meters

def ultra_tester(severity=0.5): #just controlling distance with the ultrasonic
    dist = checkdist(exact=True)
    if dist < (severity - 0.1):
        move.move_backward(60)
    elif dist > (severity + 0.1):
        move.move_forward(60)
    elif dist >= (severity - 0.1) and dist <= (severity + 0.1):
        move.motorStop()

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description = "True for with motor, false for without motor")
    ap.add_argument("with_motor", nargs='?', default=False, type=bool, help ="Do you want to test with the motor or not")    
    args = ap.parse_args()
    move.setup()
    try:
        if args.with_motor == True:
            move.setup()
            while True:
                ultra_tester(severity=0.3)
        else:
            while True:
                print(checkdist(exact=True))
    except:
        move.destroy()
        
        
