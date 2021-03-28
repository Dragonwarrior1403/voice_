import RPi.GPIO as GPIO
from time import sleep

INFRARED_FOR_BLOCK = 11
INFRARED_FOR_WALL = 8
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(INFRARED_FOR_BLOCK, GPIO.IN)
    GPIO.setup(INFRARED_FOR_WALL, GPIO.IN)

def INFRARED_FOR_WALL_FUNC():
    return GPIO.input(INFRARED_FOR_WALL)

def INFRARED_FOR_BLOCK_FUNC():
    return GPIO.input(INFRARED_FOR_BLOCK)


if __name__=="__main__":
    setup()
    while True:
        wall = INFRARED_FOR_WALL_FUNC()
        block = INFRARED_FOR_BLOCK_FUNC()
        print("WALL; {} \nBLOCK; {}".format(wall, block))
        sleep(0.5)
