"""
 " ;FileName: Rosie
 " ;Author: goat 
 " ;Created: 7/12/18
 " ;Description: Rosie the Robot!
 " ;URL
 """

import RPi.GPIO as GPIO
import time

pin = 0

# these are given relative to Rosie's perspective, her Left and Right
left_LED = 11
right_LED = 9

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(left_LED, GPIO.OUT)
GPIO.setup(right_LED, GPIO.OUT)


def main():
    while True:
        blink_lights(2, 0.3, 0.3)
        blink_lights(2, 0.3, 0.3)
        time.sleep(1)


def blink_lights(number_of_blinks, blink_on_duration, blink_off_duration):
    for x in range(1, number_of_blinks):
        #print "LEDs on"
        GPIO.output(left_LED, GPIO.HIGH)
        GPIO.output(right_LED, GPIO.HIGH)
        time.sleep(blink_on_duration)

        #print "LEDs off"
        GPIO.output(left_LED, GPIO.LOW)
        GPIO.output(right_LED, GPIO.LOW)
        time.sleep(blink_off_duration)


main()
