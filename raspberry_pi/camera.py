import cv2
import numpy as np
from pyzbar.pyzbar import decode

KNOWN_WIDTH = 5.715  # 2.25 inches in cm
FOCAL_LENGTH


def capture_image(target_barcode):
    cap = cv2.VideoCapture(0)  # Open the default camera

    while True: 
        ret, frame = cap.read()
        if not ret:
            print("Camera failed to capture image")
            break

        # convert the image to grayscale for better barcode detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        barcodes = decode(gray)

        for barcode in barcodes:
            barcode_data = barcode.data.decode('utf-8')

            if barcode_data == target_barcode:
                # send an indication to the serial port

        # camera exits if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # clean up the camera
    cap.release()
    cv2.destroyAllWindows()
            


