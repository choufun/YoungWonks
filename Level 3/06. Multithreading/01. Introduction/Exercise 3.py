'''

Given two threads, t1 blinking at one second delay, t2 blinking at half
a second delay. Observe how the threading concept works in GPIO controlling
LED

'''


# importing the threading module
import threading
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup([12,16],GPIO.OUT)
def blink1():
    while 1:
        print("blink")
        GPIO.output(12,GPIO.HIGH)
         time.sleep(1)
         print("blink")
         GPIO.output(12,GPIO.LOW)
          time.sleep(1)                         
def blinkhalf():
    while 1:
        print("blink")
        GPIO.output(16,GPIO.HIGH)
         time.sleep(0.5)
         print("blink")
         GPIO.output(16,GPIO.LOW)
         time.sleep(0.5)
# creating thread with target as the function
t1 = threading.Thread(target=blink1)
t2 = threading.Thread(target=blinkhalf)
# starting thread 1
t1.start()
# starting thread 2
t2.start()
t1.join()
t2.join()
