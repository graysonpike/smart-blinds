import time 
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
    
GpioPins = [18, 23, 24, 25]


def step(steps, interstep_delay):
    motor = RpiMotorLib.BYJMotor("BlindsStepper", "Nema")

    # TODO: Test removing this line
    time.sleep(0.5)

    if steps > 0:
        motor.motor_run(GpioPins, 0.1, steps, False, False, "full", interstep_delay)
    else:
        motor.motor_run(GpioPins, 0.1, -steps, True, False, "half", interstep_delay)


    GPIO.cleanup()
