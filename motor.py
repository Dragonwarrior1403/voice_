
#!/usr/bin/python3/

import RPi.GPIO as GPIO
import time

"""
NNOTE:!!BY DHRUV

THE SPEED HAS TO BE BETWEEN 0 AND 100.
"""
Motor_A_EN=4
Motor_B_EN=17

Motor_A_Pin1=14
Motor_A_Pin2=15
Motor_B_Pin1=27
Motor_B_Pin2=18

Dir_forward=0
Dir_backward=1

pwm_A=0
pwm_B=0

def motorStop(): # self explanatory

    GPIO.output(Motor_A_Pin1, GPIO.LOW)
    GPIO.output(Motor_A_Pin2, GPIO.LOW)
    GPIO.output(Motor_B_Pin1, GPIO.LOW)
    GPIO.output(Motor_B_Pin2, GPIO.LOW)
    GPIO.output(Motor_A_EN, GPIO.LOW)
    GPIO.output(Motor_B_EN, GPIO.LOW)

def setup():#Motor initialization
    global pwm_A, pwm_B
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Motor_A_EN, GPIO.OUT)
    GPIO.setup(Motor_B_EN, GPIO.OUT)
    GPIO.setup(Motor_A_Pin1, GPIO.OUT)
    GPIO.setup(Motor_A_Pin2, GPIO.OUT)
    GPIO.setup(Motor_B_Pin1, GPIO.OUT)
    GPIO.setup(Motor_B_Pin2, GPIO.OUT)

    motorStop()
    try:
        pwm_A = GPIO.PWM(Motor_A_EN, 1000)
        pwm_B = GPIO.PWM(Motor_B_EN, 1000)
    except:
        pass


def motor_A(direction, speed):
    if direction == Dir_backward:
        GPIO.output(Motor_B_Pin1, GPIO.HIGH)
        GPIO.output(Motor_B_Pin2, GPIO.LOW)
        pwm_A.start(100)
        pwm_A.ChangeDutyCycle(speed)
    elif direction == Dir_forward:
        GPIO.output(Motor_B_Pin1, GPIO.LOW)
        GPIO.output(Motor_B_Pin2, GPIO.HIGH)
        pwm_A.start(100)
        pwm_A.ChangeDutyCycle(speed)


def motor_B(direction, speed):
    if direction == Dir_forward:
        GPIO.output(Motor_A_Pin1, GPIO.HIGH)
        GPIO.output(Motor_A_Pin2, GPIO.LOW)
        pwm_B.start(100)
        pwm_B.ChangeDutyCycle(speed)
    elif direction == Dir_backward:
        GPIO.output(Motor_A_Pin1, GPIO.LOW)
        GPIO.output(Motor_A_Pin2, GPIO.HIGH)
        pwm_B.start(0)
        pwm_B.ChangeDutyCycle(speed)


def move_backward(speed): #  self explanantory
    GPIO.output(Motor_A_Pin1, GPIO.HIGH)
    GPIO.output(Motor_A_Pin2, GPIO.LOW)
    pwm_B.start(100)
    pwm_B.ChangeDutyCycle(speed)

    GPIO.output(Motor_B_Pin1, GPIO.LOW)
    GPIO.output(Motor_B_Pin2, GPIO.HIGH)
    pwm_A.start(100)
    pwm_A.ChangeDutyCycle(speed)

def move_forward(speed): # self explanantory
    GPIO.output(Motor_A_Pin1, GPIO.LOW)
    GPIO.output(Motor_A_Pin2, GPIO.HIGH)
    pwm_B.start(0)
    pwm_B.ChangeDutyCycle(speed)

    GPIO.output(Motor_B_Pin1, GPIO.HIGH)
    GPIO.output(Motor_B_Pin2, GPIO.LOW)
    pwm_A.start(100)
    pwm_A.ChangeDutyCycle(speed)

def turn(speedA, speedB): # self explanatory
    GPIO.output(Motor_A_Pin1, GPIO.HIGH)
    GPIO.output(Motor_A_Pin2, GPIO.LOW)
    pwm_B.start(100)
    pwm_B.ChangeDutyCycle(speedA)

    GPIO.output(Motor_B_Pin1, GPIO.LOW)
    GPIO.output(Motor_B_Pin2, GPIO.HIGH)
    pwm_A.start(100)
    pwm_A.ChangeDutyCycle(speedB)

def turn_on_spot(speed, dir):
    if dir == 'right':
        GPIO.output(Motor_A_Pin1, GPIO.LOW)
        GPIO.output(Motor_A_Pin2, GPIO.HIGH)
        pwm_B.start(0)
        pwm_B.ChangeDutyCycle(speed)

        GPIO.output(Motor_B_Pin1, GPIO.LOW)
        GPIO.output(Motor_B_Pin2, GPIO.HIGH)
        pwm_A.start(100)
        pwm_A.ChangeDutyCycle(speed)

    if dir == 'left':
        GPIO.output(Motor_B_Pin1, GPIO.HIGH)
        GPIO.output(Motor_B_Pin2, GPIO.LOW)
        pwm_A.start(100)
        pwm_A.ChangeDutyCycle(speed)

        GPIO.output(Motor_A_Pin1, GPIO.HIGH)
        GPIO.output(Motor_A_Pin2, GPIO.LOW)
        pwm_B.start(100)
        pwm_B.ChangeDutyCycle(speed)









def destroy(): # Use this function after the use of motors
    motorStop()
    GPIO.cleanup()



if __name__ == '__main__':
    setup()
    try:
        while True:
            move_forward(100)
            time.sleep(5)
            move_backward(100)
            time.sleep(5)

            turn_on_spot(50, 'left')
            time.sleep(5)
    except KeyboardInterrupt:
        destroy()
    finally:
        exit(-1)
