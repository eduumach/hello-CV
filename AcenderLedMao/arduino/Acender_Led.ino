void setup() {
  pinMode(12, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  
  if(Serial.available()){

    char ser = Serial.read();

    if(ser == 'a'){
      digitalWrite(12, LOW);
    }else if(ser == 'b'){
       digitalWrite(12, HIGH);
    }
  }

}
