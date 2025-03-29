int FRwheelPin1 = 2;
int FRwheelPin2 = 10;
int FLwheelPin1 = 3;
int FLwheelPin2 = 11;
int BRwheelPin1 = 4;
int BRwheelPin2 = 12;
int BLwheelPin1 = 5;
int BLwheelPin2 = 13;

int GearPin1 = 7;
int GearPin2 = 8;

bool commandStarted = false;
bool onGround = true;

void setup() {
  Serial.begin(115200);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB
  }
  pinMode(FRwheelPin, OUTPUT);
  pinMode(FLwheelPin, OUTPUT);
  pinMode(BRwheelPin, OUTPUT);
  pinMode(BLwheelPin, OUTPUT);
}

void loop() {
  char comm;
  
  /*
    S = command started
    G = on ground
    R = on rail
    W = move forward
    A = move right
    B = move backward
    L = move left
    G = rotate counterclockwise
    H = rotate clockwise
    U = move up
    D = move down
    E = command ended
  */
  if (Serial.available() > 0) {
    comm = Serial.read();

    // determine if within an active command sequence
    if (!commandStarted & (comm == 'S')) {
        commandStarted = true;
    } else if (commandStarted & (comm == 'E')) {
        commandStarted = false;
    }

    if (commandStarted) {
        // determine if on the ground or rail
        if (comm == 'R') {
            onGround = false;
        } else if (comm == 'G') {
            onGround = true;
        }

        if (onGround) {
            // drive forward
            if (comm == 'W') {
                digitalWrite(FRwheelPin1, HIGH);
                digitalWrite(FRwheelPin2, LOW);

                digitalWrite(FLwheelPin1, HIGH);
                digitalWrite(FLwheelPin2, LOW);

                digitalWrite(BRwheelPin1, HIGH);
                digitalWrite(BRwheelPin2, LOW);

                digitalWrite(BLwheelPin1, HIGH);
                digitalWrite(BLwheelPin2, LOW);
            // drive right
            } else if (comm = 'A') {
                digitalWrite(FRwheelPin1, LOW);
                digitalWrite(FRwheelPin2, HIGH);

                digitalWrite(FLwheelPin1, HIGH);
                digitalWrite(FLwheelPin2, LOW);

                digitalWrite(BRwheelPin1, HIGH);
                digitalWrite(BRwheelPin2, LOW);

                digitalWrite(BLwheelPin1, LOW);
                digitalWrite(BLwheelPin2, HIGH);
            // drive backward
            } else if (comm = 'B') {
                digitalWrite(FRwheelPin1, LOW);
                digitalWrite(FRwheelPin2, HIGH);

                digitalWrite(FLwheelPin1, LOW);
                digitalWrite(FLwheelPin2, HIGH);

                digitalWrite(BRwheelPin1, LOW);
                digitalWrite(BRwheelPin2, HIGH);

                digitalWrite(BLwheelPin1, LOW);
                digitalWrite(BLwheelPin2, HIGH);
            // drive left
            } else if (comm = 'L') {
                digitalWrite(FRwheelPin1, HIGH);
                digitalWrite(FRwheelPin2, LOW);

                digitalWrite(FLwheelPin1, LOW);
                digitalWrite(FLwheelPin2, HIGH);

                digitalWrite(BRwheelPin1, LOW);
                digitalWrite(BRwheelPin2, HIGH);

                digitalWrite(BLwheelPin1, HIGH);
                digitalWrite(BLwheelPin2, LOW);
            // rotate counterclockwise
            } else if (comm = 'G') {
                digitalWrite(FRwheelPin1, LOW);
                digitalWrite(FRwheelPin2, HIGH);

                digitalWrite(FLwheelPin1, HIGH);
                digitalWrite(FLwheelPin2, LOW);

                digitalWrite(BRwheelPin1, LOW);
                digitalWrite(BRwheelPin2, HIGH);

                digitalWrite(BLwheelPin1, HIGH);
                digitalWrite(BLwheelPin2, LOW);
            // rotate clockwse
            } else if (comm = 'H') {
                digitalWrite(FRwheelPin1, HIGH);
                digitalWrite(FRwheelPin2, LOW);

                digitalWrite(FLwheelPin1, LOW);
                digitalWrite(FLwheelPin2, HIGH);

                digitalWrite(BRwheelPin1, HIGH);
                digitalWrite(BRwheelPin2, LOW);

                digitalWrite(BLwheelPin1, LOW);
                digitalWrite(BLwheelPin2, HIGH);
            }
        } else {
            // move up
            if (comm == 'U') {
                digitalWrite(GearPin1, HIGH);
                digitalWrite(GearPin2, LOW);
            // move down
            } else if (comm == 'D') {
                digitalWrite(GearPin1, LOW);
                digitalWrite(GearPin2, HIGH);
            }
        }
    } else { // if no command is being sent, stop all motion
        digitalWrite(FRwheelPin1, LOW);
        digitalWrite(FRwheelPin2, LOW);

        digitalWrite(FLwheelPin1, LOW);
        digitalWrite(FLwheelPin2, LOW);

        digitalWrite(BRwheelPin1, LOW);
        digitalWrite(BRwheelPin2, LOW);

        digitalWrite(BLwheelPin1, LOW);
        digitalWrite(BLwheelPin2, LOW);
        
        digitalWrite(GearPin1, LOW);
        digitalWrite(GearPin2, LOW);
    }
}
