#include <SoftwareSerial.h>

const byte MAX_ESC = 220;
const byte MIN_ESC = 120;
const byte rx = 8;
const byte tx = 9;
const byte ESC = 3;
SoftwareSerial BT(rx,tx);

void setup() {
  // put your setup code here, to run once:
  BT.begin(9600);
  Serial.begin(9600);
  pinMode(rx,INPUT);
  Serial.println("test");

  pinMode(ESC, OUTPUT);
  analogWrite(ESC, 0);
}

void loop() {
  // put your main code here, to run repeatedly:
  int choice = Serial.read();
  if(choice = 116){
      calibrate();
  }
}

void calibrate(){
  
  Serial.println("Beginning calibration.");
  Serial.println("First, disconnect the battery.");
  Serial.println("Enter 'c' when disconnected");
  
  int completed = 0;
  while(completed != 99){ //will stay in while loop until c (ASCII 99) is entered
    completed = Serial.read();
    if(BT.available() >= 1){
      completed = BT.read();
    }
  }

  analogWrite(ESC,MAX_ESC); //analog write
  Serial.println(MAX_ESC); 
  delay(1000);
  
  Serial.println("Now, plug in the battery. You will hear a series of beeps.");
  Serial.println("Enter 'c' after 3 beeps");
  completed = 0;
  while(completed != 99){
    completed = Serial.read();
    if(BT.available() >= 1){
      completed = BT.read();
    }
  }

  analogWrite(ESC,MIN_ESC);
  Serial.println(MIN_ESC);
  delay(1000);

  Serial.println("Wait for this pattern: 2 short beeps, then 2 long beeps.");
  Serial.println("After you hear this pattern, disconnect the battery again.");
  Serial.println("Enter 'c' when disconnected:");
  completed = 0;
  while(completed != 99){
    completed = Serial.read();
    if(BT.available() >= 1){
      completed = BT.read();
    }
  }

  delay(1000);
  Serial.println("Now, plug the battery back in.");
  Serial.println("You should hear 3 short beeps, then a low beep and a high beep.");
  Serial.println("If you hear this, then calibration was successful.");
  delay(1000);
  
}

void test_speeds(){
  int ctrl = 120;
  while(ctrl != 
  int ctrl = 120;
  
}
