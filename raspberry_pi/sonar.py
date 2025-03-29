import RPi.GPIO as GPIO
import time

# signal to send pulse
BOTTOM_TRIG = #### #coordinate to pin number
SIDE_TRIG = #### #coordinate to pin number

# used to measure the time it takes for the sound to travel to the object and back
BOTTOM_ECHO = #### # coordinate to pin number
SIDE_ECHO = #### # coordinate to pin number

GPIO.setmode(GPIO.BOARD) # physical pin numbering
GPIO.setup(BOTTOM_TRIG, GPIO.OUT) # trigger pin as output
GPIO.setup(BOTTOM_ECHO, GPIO.IN) # echo pin as input
GPIO.setup(SIDE_TRIG, GPIO.OUT) # trigger pin as output
GPIO.setup(SIDE_ECHO, GPIO.IN) # echo pin as input


def get_distance(sensor):

    if (sensor == "bottom"):
        TRIG_PIN = BOTTOM_TRIG
        ECHO_PIN = BOTTOM_ECHO
    else:
        TRIG_PIN = BOTTOM_ECHO
        ECHO_PIN = SIDE_ECHO

    # set to low trigger pin for 2 seconds
    GPIO.output(TRIG_PIN, False)
    time.sleep(0.1)

    # set to high trigger pin for 10 microseconds
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)

    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = (pulse_duration * 34300)/ 2 # speed of sound = 343 m/s

    return round(distance,2)