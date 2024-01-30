// ir initialization
int ir1 = 8; // rigth most
int ir2 = 9; // second from right 
int ir3 = 10; // second from left 
int ir4 = 11; // left most 

// motor driver intialization
int motordrive1 = 3; // leftmost motor 
int motordrive2 = 4; // second from left 
int motordrive3 = 5; // second from right 
int motordrive4 = 6; // rightmost motor 

// remove the jumpers to speed control the line follower
int enA= A0;
int enB = A1;

void setup(){
  Serial.begin(9600);
  pinMode(ir1, INPUT);
  pinMode(ir2, INPUT);
  pinMode(ir3, INPUT);
  pinMode(ir4, INPUT);
  pinMode(motordrive1, OUTPUT);
  pinMode(motordrive2, OUTPUT);
  pinMode(motordrive3, OUTPUT);
  pinMode(motordrive4, OUTPUT);
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
}

void loop(){
  int IR1= digitalRead(ir1);
  int IR2= digitalRead(ir2);
  int IR3= digitalRead(ir3);
  int IR4= digitalRead(ir4);
  Serial.println('rigth to left');  
  Serial.println(IR1);
  Serial.println(IR2);
  Serial.println(IR3);
  Serial.println(IR4);
  
  if (IR4== HIGH && IR3== HIGH && IR2== HIGH && IR1== HIGH){ // off track and u-turn
        digitalWrite(motordrive1,HIGH); 
        digitalWrite(motordrive2,LOW);
        digitalWrite(motordrive3,HIGH);
        digitalWrite(motordrive4,LOW);
        analogWrite(enA,0);
        analogWrite(enB,0);
        delayMicroseconds(2000);
        analogWrite(enA,200);
        analogWrite(enB,100);
        delayMicroseconds(2000);
        analogWrite(enA,255);
        analogWrite(enB,255);
  }
  
  else if (IR4== HIGH && IR3== LOW && IR2== LOW && IR1== HIGH){ // move forward
        digitalWrite(motordrive1,HIGH);
        digitalWrite(motordrive2,LOW);
        digitalWrite(motordrive3,HIGH);
        digitalWrite(motordrive4,LOW);
        analogWrite(enA,255);
        analogWrite(enB,255);
  }
  else if (IR4== HIGH && IR3== LOW && IR2== LOW && IR1== LOW){ // turn right 
       digitalWrite(motordrive1,HIGH);
       digitalWrite(motordrive2,LOW);
       digitalWrite(motordrive3,LOW);
       digitalWrite(motordrive4,LOW);
       analogWrite(enA,255);
       analogWrite(enB,100);
  }
  else if (IR4== LOW && IR3== LOW && IR2== LOW && IR1== HIGH){ // turn left
       digitalWrite(motordrive1,LOW);
       digitalWrite(motordrive2,LOW);
       digitalWrite(motordrive3,HIGH);
       digitalWrite(motordrive4,LOW);
       analogWrite(enA,100);
       analogWrite(enB,255);
  }
  else if (IR4== LOW && IR3== LOW && IR2== LOW && IR1== LOW){ // stop 
      digitalWrite(motordrive1,LOW);
      digitalWrite(motordrive2,LOW);
      digitalWrite(motordrive3,LOW);
      digitalWrite(motordrive4,LOW);
      analogWrite(enA,0);
      analogWrite(enB,0);
  }
}