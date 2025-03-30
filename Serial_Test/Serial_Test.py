import serial

if __name__ == "__main__":
    ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
    ser.setDTR(False)
    ser.flushInput()
    ser.setDTR(True)

    i = 0
    while True:
        if (0 < i & i < 1000):
            ser.write(b'R')
        elif (1000 < i & i < 2000):
            ser.write(b'G')
        else:
            ser.write(b'B')
        i += 1

        if(i == 3000):
            i = 0