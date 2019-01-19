import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)

if sys.argv[1] == '0':
    print('OFF')
    GPIO.output(4,GPIO.HIGH)
else:
    print('ON')
    GPIO.output(4,GPIO.LOW)
