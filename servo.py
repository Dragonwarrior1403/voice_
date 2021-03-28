import Adafruit_PCA9685
import time

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

pwm0_grab = 400
pwm0_release = 150

pwm1_grab = 400
pwm1_release = 600




def Grabbeer_left_grab():
    pwm.set_pwm(0, 0, pwm0_grab)

def Grabber_right_grab():
    pwm.set_pwm(1, 0, pwm1_grab)

def Grab():
    Grabbeer_left_grab()
    Grabber_right_grab()

def Release():
    pwm.set_pwm(0, 0, pwm0_release)
    pwm.set_pwm(1, 0, pwm1_release)

if __name__ == '__main__':
    
    Grab()
    time.sleep(1)
    
    Release()
    time.sleep(1)
    
