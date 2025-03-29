import cv2
import serial
import time
import numpy as np

import raspberry_pi.sonar as sonar # get_distance(sensor)

import raspberry_pi.camera as camera # capture_image(target_barcode), detect_barcode(img_frame, grayscale, target_barcode)

# COMMUNICATING WITH ARDUINO:
#
# S = command started
# G = on ground
# R = on rail
# W = move forward
# A = move right
# B = move backward
# L = move left
# G = rotate counterclockwise
# H = rotate clockwise
# U = move up
# D = move down
# E = command ended

# ser.write(b'S')

class Robot():
    def __init__(self):
        self.lockedDistance = 3

        self.onRail = False
        self.target_barcode = 0
        self.target_shelf_height = 0
        self.camera = 0

        self.ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
        self.ser.setDTR(False)
        self.ser.flushInput()
        self.ser.setDTR(True)

    def define_goal(self, asin):
        self.target_barcode = asin["shelf_barcode"]
        self.target_shelf_height = asin["shelf_height"]

    def move_to_goal(self):
        self.camera = cv2.VideoCapture(0)
        self.ground_search()
        self.rail_search()
        self.camera.release()
        cv2.destroyAllWindows()

    def ground_search(self):
        self.ser.write(b'S')
        self.ser.write(b'G')

        # line up with rail horizontally
        while True:
            frame = camera.capture_image(self.camera)
            cv2.imshow('Camera Feed', frame)
            hypotenuse = camera.detect_barcode(frame, self.target_barcode, self.onRail)
            vertical_distance = sonar.get_distance("front")
            horizontal_distance = np.sqrt(hypotenuse*hypotenuse - vertical_distance*vertical_distance)
            if (abs(horizontal_distance) > 5):

                # detect a drift
                if (abs(vertical_distance - prev_vertical_distance) > self.driftThreshold):
                    if (vertical_distance > prev_vertical_distance):
                        self.ser.write(b'H')
                    else:
                        self.ser.write(b'J')
                if (hypotenuse > 0):
                    self.ser.write(b'L')
                else:
                    self.ser.write(b'A')
            else:
                break

            prev_vertical_distance = vertical_distance
        
        # lock in to rail
        while(True):
            distance = sonar.get_distance("front")
            if (distance > self.lockedDistance):
                self.ser.write(b'W')
            else:
                break

        self.ser.write(b'E')

    def rail_search(self):
        while True:
            

def __name__ == "__main__":
    rob1 = Robot()
    asin = {
        "shelf_barcode" : 0,
        "shelf_height" : 0
    }
    rob1.define_goal(asin)
    rob1.move_to_goal()