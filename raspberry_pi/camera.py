import cv2
import numpy as np
from pyzbar.pyzbar import decode

# assume that we are assuming no boxes are the same width as the rail
KNOWN_WIDTH = 5.715  # 2.25 inches in cm
FOCAL_LENGTH = # camera dependent value

def detect_rail(img_frame, grayscale):
    # apply gaussian blur to reduce small noise
    blurred = cv2.GaussianBlur(grayscale, (9, 9), 2)

    # apply canny edge detection to find edges in the image
    edges = cv2.Canny(blurred, 50, 150)

    # dilate edges to focus on larger contours
    kernel = np.ones((5,5), np.uint8)
    dilated = cv2.dilate(edges, kernel, iteration = 1)

    # find contours in the image
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    railing_width_px = 0
    for contour in contours:
        x,y,w,h = cv2.boundingRect(contour)

        if w > KNOWN_WIDTH + .2 or w < KNOWN_WIDTH - .2:
            cv2.rectangle(img_frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
            railing_width_px = max(railing_width_px, w)

    if railing_width_px > 0:
        distance = (KNOWN_WIDTH * FOCAL_LENGTH) / railing_width_px
        # add calculations to adjust distance to the rail
        # send indication to the serial port


def detect_barcode(img_frame, grayscale, target_barcode):
    barcodes = decode(grayscale)

    for barcode in barcodes:
        barcode_data = barcode.data.decode('utf-8')

        if barcode_data == target_barcode:
            # send an indication to the serial port
            detect_rail(img_frame, grayscale)


def capture_image(target_barcode):
    cap = cv2.VideoCapture(0)  # Open the default camera

    while True: 
        ret, frame = cap.read()
        if not ret:
            print("Camera failed to capture image")
            break

        # convert the image to grayscale for better barcode detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        detect_barcode(frame, gray, target_barcode)
        
        # camera exits if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # clean up the camera
    cap.release()
    cv2.destroyAllWindows()
            


