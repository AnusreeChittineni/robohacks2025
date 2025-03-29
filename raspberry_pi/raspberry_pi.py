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
        self.lineUpThreshold = 5
        self.driftThreshold = 20
        self.heightThreshold = 0.5

        self.onRail = False
        self.target_shelf_barcode = 0
        self.target_bin_barcode = 0
        self.camera = 0

        self.ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
        self.ser.setDTR(False)
        self.ser.flushInput()
        self.ser.setDTR(True)

    def define_goal(self, asin):
        self.target_shelf_barcode = asin["shelf_barcode"]
        self.target_bin_barcode = asin["bin_barcode"]

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
            hypotenuse = camera.detect_barcode(frame, self.target_shelf_barcode, self.onRail)

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
        self.ser.write(b'G')

        # move to shelf
        while True:
            frame = camera.capture_image(self.camera)
            cv2.imshow('Camera Feed', frame)
            vertical_distance =  camera.detect_barcode(frame, self.target_bin_barcode, self.onRail)

            if (vertical_distance[1]):
                if (abs(vertical_distance) < self.heightThreshold):
                    break
                elif (vertical_distance > 0):
                    self.ser.write(b'D')
                else:
                    self.ser.write(b'U')
            else:
                self.ser.write(b'U')

        self.ser.write(b'E')

if __name__ == "__main__":
    rob1 = Robot()
    asin = {
        "shelf_barcode" : 0,
        "bin_barcode" : 0
    }
    rob1.define_goal(asin)
    rob1.move_to_goal()