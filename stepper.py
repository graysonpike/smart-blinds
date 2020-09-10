import time 
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
    
GpioPins = [18, 23, 24, 25]


def adjust(steps, interstep_delay):
    motor = RpiMotorLib.BYJMotor("BlindsStepper", "Nema")

    # TODO: Test removing this line
    time.sleep(0.5)

    motor.motor_run(GpioPins, 0.1, steps, False, False, "half", interstep_delay)

    GPIO.cleanup()
