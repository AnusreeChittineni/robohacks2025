int FRwheelPin1 = 4;
int FRwheelPin2 = 5;
int FLwheelPin1 = 2;
int FLwheelPin2 = 3;
int BRwheelPin1 = 8;
int BRwheelPin2 = 9;
int BLwheelPin1 = 6;
int BLwheelPin2 = 7;

int GearPin1 = 12;
int GearPin2 = 13;

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
    H = rotate counterclockwise
    J = rotate clockwise
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
            if (comm == 'W') {
                goForward();
            } else if (comm = 'A') {
                goRight();
            } else if (comm = 'B') {
                goBackward();
            } else if (comm = 'L') {
                goLeft();
            } else if (comm = 'H') {
                rotateCCW();
            } else if (comm = 'J') {
                rotateCW();
            }
        } else {
            if (comm == 'U') {
                goUp();
            } else if (comm == 'D') {
                goDown();
            }
        }
    } else { // if no command is being sent, stop all motion
        breakAll();
    }
}

void goForward() {
    digitalWrite(FRwheelPin1, HIGH);
    digitalWrite(FRwheelPin2, LOW);

    digitalWrite(FLwheelPin1, HIGH);
    digitalWrite(FLwheelPin2, LOW);

    digitalWrite(BRwheelPin1, HIGH);
    digitalWrite(BRwheelPin2, LOW);

    digitalWrite(BLwheelPin1, HIGH);
    digitalWrite(BLwheelPin2, LOW);
}

void goBackward() {
    digitalWrite(FRwheelPin1, LOW);
    digitalWrite(FRwheelPin2, HIGH);

    digitalWrite(FLwheelPin1, LOW);
    digitalWrite(FLwheelPin2, HIGH);

    digitalWrite(BRwheelPin1, LOW);
    digitalWrite(BRwheelPin2, HIGH);

    digitalWrite(BLwheelPin1, LOW);
    digitalWrite(BLwheelPin2, HIGH);
}

void goLeft() {
    digitalWrite(FRwheelPin1, HIGH);
    digitalWrite(FRwheelPin2, LOW);

    digitalWrite(FLwheelPin1, LOW);
    digitalWrite(FLwheelPin2, HIGH);

    digitalWrite(BRwheelPin1, LOW);
    digitalWrite(BRwheelPin2, HIGH);

    digitalWrite(BLwheelPin1, HIGH);
    digitalWrite(BLwheelPin2, LOW);
}

void goRight() {
    digitalWrite(FRwheelPin1, LOW);
    digitalWrite(FRwheelPin2, HIGH);

    digitalWrite(FLwheelPin1, HIGH);
    digitalWrite(FLwheelPin2, LOW);

    digitalWrite(BRwheelPin1, HIGH);
    digitalWrite(BRwheelPin2, LOW);

    digitalWrite(BLwheelPin1, LOW);
    digitalWrite(BLwheelPin2, HIGH);
}

void rotateCW() {
    digitalWrite(FRwheelPin1, HIGH);
    digitalWrite(FRwheelPin2, LOW);

    digitalWrite(FLwheelPin1, LOW);
    digitalWrite(FLwheelPin2, HIGH);

    digitalWrite(BRwheelPin1, HIGH);
    digitalWrite(BRwheelPin2, LOW);

    digitalWrite(BLwheelPin1, LOW);
    digitalWrite(BLwheelPin2, HIGH);
}

void rotateCCW() {
    digitalWrite(FRwheelPin1, LOW);
    digitalWrite(FRwheelPin2, HIGH);

    digitalWrite(FLwheelPin1, HIGH);
    digitalWrite(FLwheelPin2, LOW);

    digitalWrite(BRwheelPin1, LOW);
    digitalWrite(BRwheelPin2, HIGH);

    digitalWrite(BLwheelPin1, HIGH);
    digitalWrite(BLwheelPin2, LOW);
}

void goUp() {
    digitalWrite(GearPin1, HIGH);
    digitalWrite(GearPin2, LOW);
}

void goDown() {
    digitalWrite(GearPin1, LOW);
    digitalWrite(GearPin2, HIGH);
}

void breakAll() {
    digitalWrite(FRwheelPin1, HIGH);
    digitalWrite(FRwheelPin2, HIGH);

    digitalWrite(FLwheelPin1, HIGH);
    digitalWrite(FLwheelPin2, HIGH);

    digitalWrite(BRwheelPin1, HIGH);
    digitalWrite(BRwheelPin2, HIGH);

    digitalWrite(BLwheelPin1, HIGH);
    digitalWrite(BLwheelPin2, HIGH);
    
    digitalWrite(GearPin1, HIGH);
    digitalWrite(GearPin2, HIGH);
}
}