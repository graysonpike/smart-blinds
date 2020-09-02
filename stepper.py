import time 
import RPi.GPIO as GPIO

# This code snippet is for Version 1.2 

# import the library
from RpiMotorLib import RpiMotorLib
    
GpioPins = [12, 16, 18, 22]

# Declare an named instance of class pass a name and type of motor
mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "Nema")
time.sleep(0.5)

# call the function pass the parameters
mymotortest.motor_run(GpioPins , 0.1, 50, False, False, "half", .05)

# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()
