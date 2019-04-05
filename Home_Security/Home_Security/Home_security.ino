void setup() {
  // put your setup code here, to run once:
pinMode(A0,INPUT_PULLUP);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
int sw=digitalRead(A0);

if(sw==0)
{
  while(digitalRead(A0)==0);
  Serial.print("send");
  delay(1000);
}


  
}
