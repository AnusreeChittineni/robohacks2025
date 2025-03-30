int WheelPin1 = 8;
int WheelPin2 = 9;

int GearPin1 = 12;
int GearPin2 = 13;

bool commandStarted = false;
bool onGround = true;

void setup() {
//   Serial.begin(115200);
//   while (!Serial) {
//     ; // wait for serial port to connect. Needed for native USB
//   }
  pinMode(WheelPin1, OUTPUT);
  pinMode(WheelPin2, OUTPUT);
  pinMode(GearPin1, OUTPUT);
  pinMode(GearPin2, OUTPUT);
}

void loop() {
  char comm;
  
  /*
    S = command started
    G = on ground
    R = on rail
    W = move forward
    A = turn left
    F = turn right
    U = move up
    D = move down
    E = command ended
  */
  digitalWrite(WheelPin1, HIGH);
  digitalWrite(WheelPin2, LOW);

  delay(1000);

  digitalWrite(WheelPin1, HIGH);
  digitalWrite(WheelPin2, HIGH);

  delay(1000);

  digitalWrite(GearPin1, HIGH);
  digitalWrite(GearPin2, LOW);

  delay(2500);

  digitalWrite(GearPin1, HIGH);
  digitalWrite(GearPin2, HIGH);

  while (true) {
    continue;
  }
}
//                 digitalWrite(WheelPin2, LOW);
//                 digitalWrite(WheelPin2, LOW);
//   if (Serial.available() > 0) {
//     comm = Serial.read();

//     // determine if within an active command sequence
//     if (!commandStarted & (comm == 'S')) {
//         commandStarted = true;
//     } else if (commandStarted & (comm == 'E')) {
//         commandStarted = false;
//     }

//     if (commandStarted) {
//         // determine if on the ground or rail
//         if (comm == 'R') {
//             onGround = false;
//         } else if (comm == 'G') {
//             onGround = true;
//         }

//         if (onGround) {
//             if (comm == 'A') {
//                 digitalWrite(WheelPin1, HIGH);
//                 digitalWrite(WheelPin2, LOW);
//             } else if (comm = 'F') {
//                 digitalWrite(WheelPin1, LOW);
//                 digitalWrite(WheelPin2, HIGH);
//             }
//         } else {
//             if (comm == 'U') {
//                 goUp();
//             } else if (comm == 'D') {
//                 goDown();
//             }
//         }
//     } else { // if no command is being sent, stop all motion
//         breakAll();
//     }
// }

void goUp() {
    digitalWrite(GearPin1, HIGH);
    digitalWrite(GearPin2, LOW);
}

void goDown() {
    digitalWrite(GearPin1, LOW);
    digitalWrite(GearPin2, HIGH);
}

void breakAll() {
    digitalWrite(WheelPin1, HIGH);
    digitalWrite(WheelPin2, HIGH);
    
    digitalWrite(GearPin1, HIGH);
    digitalWrite(GearPin2, HIGH);
}