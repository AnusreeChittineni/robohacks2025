import serial
import time
import numpy as np

import sonar # get_distance(sensor)

import camera # capture_image(target_barcode), detect_barcode(img_frame, grayscale, target_barcode)

import cv2
from picamera2 import Picamera2


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
        self.lineUpThreshold = 5
        self.driftThreshold = 20
        self.heightThreshold = 0.5
        self.moveUpLoops = 3

        self.onRail = False
        self.target_marker_ids = 0
        self.target_bin_marker_id = 0
        self.camera = 0

        self.ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
        self.ser.setDTR(False)
        self.ser.flushInput()
        self.ser.setDTR(True)

    def define_goal(self, asin):
        self.target_shelf_marker_id = asin["shelf_marker_id"]
        self.target_bin_marker_id = asin["bin_marker_id"]

    def move_to_goal(self):
        picam2 = Picamera2()
        picam2.configure(picam2.create_preview_configuration())
        self.camera = picam2.start()
        self.ground_search()
        self.rail_search()
        self.camera.release()
        cv2.destroyAllWindows()

    def ground_search(self):
        self.ser.write(b'S')
        self.ser.write(b'G')

        # line up with rail horizontally
        while True:
            frame = camera.capture_image()
            cv2.imshow('Camera Feed', frame)
            hypotenuse = camera.detect_aruco_marker(frame, self.target_shelf_marker_id, self.onRail)

            if hypotenuse[1]:
                lateral_distance = sonar.get_distance("front")
                horizontal_distance = np.sqrt(hypotenuse[0]*hypotenuse[0] - lateral_distance*lateral_distance)
                if (abs(horizontal_distance) > self.lineUpThreshold):

                    # detect a drift, for demo purposes this will not be used
                    # if (abs(lateral_distance - prev_lateral_distance) > self.driftThreshold):
                    #     if (lateral_distance > prev_lateral_distance):
                    #         self.ser.write(b'H')
                    #     else:
                    #         self.ser.write(b'J')
                    if (hypotenuse > 0):
                        self.ser.write(b'W')
                    else:
                        self.ser.write(b'B')
                else:
                    break
                prev_lateral_distance = lateral_distance
            else:
                self.ser.write(b'W')
        
        # lock in to rail
        while(True):
            distance = sonar("front")
            if (distance > self.lockedDistance):
                self.ser.write(b'L')
            else:
                break

        self.ser.write(b'E')

    def rail_search(self):
        self.ser.write(b'S')
        self.ser.write(b'R')

        # move to bin
        while True:
            frame = camera.capture_image()
            cv2.imshow('Camera Feed', frame)
            vertical_distance =  camera.detect_aruco_marker(frame, self.target_bin_marker_id, self.onRail)

            if (vertical_distance[1]):
                if (abs(vertical_distance) < self.heightThreshold):
                    break
                elif (vertical_distance > 0):
                    self.ser.write(b'U')
                else:
                    self.ser.write(b'D')
            else:
                self.ser.write(b'U')

        self.ser.write(b'E')

if __name__ == "__main__":
    rob1 = Robot()
    asin = {
        "shelf_barcode" : 0x000E247408100,
        "bin_barcode" : 0x000E366CA8A00
    }
    rob1.define_goal(asin)
    rob1.move_to_goal()