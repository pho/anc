/*
  NES Controller 
 
 CLK -> Pin 2
 LATCH -> Pin 3
 DATA -> Pin 4
 
 */

int CLK = 2;
int L = 3;
int DATA= 4;
int BUTTONS[8] = {0,0,0,0,0,0,0,0};


void setup()   {                

  Serial.begin(9600);
  Serial.print("READY!\n");
  
  pinMode(CLK, OUTPUT);
  pinMode(L, OUTPUT);
  pinMode(DATA, INPUT); 
  
  digitalWrite(L, LOW);
  digitalWrite(CLK, LOW);
}


void loop()                     
{
 if (Serial.read() == 'a'){; // Wait for sync byte
  digitalWrite(L, HIGH);   // Grab the buttons
  digitalWrite(L, LOW);
  
  for ( int i = 0; i < 8; i++){
    
    BUTTONS[i] = digitalRead(DATA);
    
    digitalWrite(CLK, HIGH);   // Generate CLK
    digitalWrite(CLK, LOW);
  }
  
  for ( int i = 0; i < 8; i++){
    Serial.print(BUTTONS[i]); // Send the buttons
  }
  
  Serial.print("\n");
  
 }
}  
 
