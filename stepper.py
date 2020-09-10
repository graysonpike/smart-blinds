import time 
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
    
GPIO_PINS = [18, 23, 24, 25]
GPIO_INIT_WAIT = 0.01


def step(steps, interstep_delay):
    motor = RpiMotorLib.BYJMotor("BlindsStepper", "Nema")

    # TODO: Test removing this line
    time.sleep(0.5)

    if steps > 0:
        motor.motor_run(GPIO_PINS, interstep_delay, steps, False, False, "full", GPIO_INIT_WAIT)
    else:
        motor.motor_run(GPIO_PINS, interstep_delay, -steps, True, False, "half", GPIO_INIT_WAIT)


    GPIO.cleanup()
