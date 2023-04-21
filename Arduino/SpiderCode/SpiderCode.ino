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

  pinMode(ESC, OUTPUT);
  analogWrite(ESC, MIN_ESC);

  menu();
}

void menu() {
  Serial.println("Choose a program to execute:");
  Serial.println("c - Calibrate");
  Serial.println("a - Arm");
  Serial.println("t - Test");
  Serial.println("d - Drive");
}

void loop() {
  // put your main code here, to run repeatedly:
  int choice = Serial.read();
  if (choice == 99) {
      calibrate();
  }
  else if (choice == 97) {
      arm();
  }
  else if (choice == 116) {
      test_speed();
  }
  else if (choice == 100) {
      drive();
  }
}

void calibrate(){
  
  Serial.println("Beginning calibration.");
  Serial.println("First, disconnect the battery from the ESC.");
  Serial.println("Enter 'c' when disconnected");
  
  int completed = 0;
  while(completed != 99){ //will stay in while loop until c (ASCII 99) is entered
    completed = Serial.read();
    if(BT.available() >= 1){
      completed = BT.read();
    }
  }

  analogWrite(ESC,MAX_ESC); //analog write
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
  
  menu();
}

void arm() {
  
  Serial.println("Begining arm.");
  Serial.println("First, disconnect the battery from the ESC.");
  Serial.println("Enter 'c' when disconnected");
  
  int completed = 0;
  while(completed != 99){ //will stay in while loop until c (ASCII 99) is entered
    completed = Serial.read();
    if(BT.available() >= 1){
      completed = BT.read();
    }
  }

  analogWrite(ESC,MIN_ESC); //analog write
  delay(1000);

  Serial.println("Now, plug in the battery. You will hear a low beep, then a high beep.");
  Serial.println("If you do, arming was successful.");
  delay(1000);

  menu();
}

void test_speed(){
  int speed = MIN_ESC;
  int ctrl = 0;

  Serial.println("Testing mode");
  Serial.println("u - Speed up by 30%");
  Serial.println("d - Speed down by 30%");
  Serial.println("e - Exit");

  Serial.println(speed - MIN_ESC);
  
  while (ctrl != 101){ //e for escape
    
    ctrl = 0;
    while (ctrl != 117 && ctrl != 100 && ctrl != 101){ //waits for valid input
      ctrl = Serial.read(); 
    }
    if (ctrl == 117){ //u
      speed = min(speed + 30, MAX_ESC);
      Serial.println(speed - MIN_ESC);
    }
    else if(ctrl == 100){ //d
      speed = max(speed - 30, MIN_ESC);
      Serial.println(speed - MIN_ESC);
    }
    analogWrite(ESC,speed);
  }

  menu();
}

void drive(){
  int choice = 0;

  if (BT.available() >= 1){
    //delay(200);
    int choice = BT.read();
    if (choice == 115){ //backwards s
      digitalWrite(10,HIGH);
      digitalWrite(11,HIGH);
      digitalWrite(5,LOW);
      digitalWrite(6,HIGH);
      digitalWrite(2,LOW);
      digitalWrite(3,HIGH);
      //delay(100);
    }
    else if (choice == 119){ //forward w
      digitalWrite(10,HIGH);
      digitalWrite(11,HIGH);
      digitalWrite(6,LOW);
      digitalWrite(5,HIGH);
      digitalWrite(3,LOW);
      digitalWrite(2,HIGH);
      //delay(100);
    }
    else if(choice == 32){ //stop space
      digitalWrite(10,HIGH);
      digitalWrite(11,HIGH);
      digitalWrite(5,LOW);
      digitalWrite(6,LOW);
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
      //delay(100);
    }
    else if (choice == 97){ //left a
      digitalWrite(10,HIGH);
      digitalWrite(11,HIGH);
      digitalWrite(5,HIGH);
      digitalWrite(6,LOW);
      digitalWrite(2,LOW);
      digitalWrite(3,HIGH);
      //delay(100);
    }
     else if (choice == 100){ //right d
      digitalWrite(10,HIGH);
      digitalWrite(11,HIGH);
      digitalWrite(5,HIGH);
      digitalWrite(6,LOW);
      digitalWrite(2,LOW);
      digitalWrite(3,HIGH);
      //delay(100)
    Serial.print(choice);
    }
  }
  menu();
}
