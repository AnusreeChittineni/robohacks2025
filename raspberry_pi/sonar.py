import RPi.GPIO as GPIO
import time

# signal to send pulse
TRIG = #### #coordinate to pin number

# used to measure the time it takes for the sound to travel to the object and back
ECHO = #### # coordinate to pin number

GPIO.setmode(GPIO.BOARD) # physical pin numbering
GPIO.setup(TRIG, GPIO.OUT) # trigger pin as output
GPIO.setup(ECHO, GPIO.IN) # echo pin as input


def get_distance():

    # set to low trigger pin for 2 seconds
    GPIO.output(TRIG, False)
    time.sleep(0.1)

    # set to high trigger pin for 10 microseconds
    GPIO.output(TRIG, True)
    time.sleep(0.00001)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = (pulse_duration * 34300)/ 2 # speed of sound = 343 m/s

    return round(distance,2)