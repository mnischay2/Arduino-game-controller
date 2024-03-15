void setup() {
pinMode(A0,INPUT);  // X-axis 
pinMode(A1,INPUT);  // Y-axis

pinMode(12,INPUT);  // Switch reading pin

pinMode(2,OUTPUT);  // red led

Serial.begin(9600);
}
void loop() {
  
int s= digitalRead(12); // reading switch
if(s==1){ // if switch on
  digitalWrite(2,0); // powering off the red led  
  digitalWrite(3,1); // powering on the green led  
int x=analogRead(A0); // reading the X-axis
int y=analogRead(A1); // reading the Y-axis

  if(((x>=325) && (x<=350)) && ((y>=370) && (y<=410))){ // forward
    Serial.println("w"); 
 }

else if(((x>=325) && (x<=350)) && ((y>=270) && (y<=315))){ // backward
    Serial.println("s"); 
 }

else if(((y>=325) && (y<=350)) && ((x>=370) && (x<=410))){ //right
    Serial.println("d"); 
 }

else if(((y>=325) && (y<=350)) && ((x>=270) && (x<=315))){ // left
    Serial.println("a"); 
 }
 else{
  Serial.println("p"); 
 }
}
else{ //if switch off
  digitalWrite(2,1); // powering on the red led  
  digitalWrite(3,0); // powering off the green led  
}
 
}
