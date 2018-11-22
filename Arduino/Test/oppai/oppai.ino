const int val_size = 4;
int values[val_size] = {123, 456, 789, 100};

void setup(){
  Serial.begin(9600);
}

void loop(){
  for (int i=0; i<val_size; i++){
    int high = (values[i] >> 7) & 127;
    int low  = values[i] & 127;
    Serial.write(128+i);
    Serial.write(high);
    Serial.write(low);
  }
}
