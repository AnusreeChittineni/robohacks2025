import serial
import time

import raspberry_pi.sonar as sonar # get_distance(sensor)

import raspberry_pi.camera as camera # capture_image(target_barcode)

# initalize a serial communication connection
ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)

# https://rimstar.org/science_electronics_projects/raspberry_pi_to_arduino_serial_usb_communication.htm
ser.setDTR(False)
time.sleep(3)
ser.flushInput()
ser.setDTR(True)
time.sleep(2)

# ser.write(b'S')

while True:
