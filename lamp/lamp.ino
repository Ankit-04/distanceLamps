#include <LiquidCrystal.h>
LiquidCrystal lcd(3, 4, 5, 6, 7, 8);

String data;
String messg;
String redVal, greenVal, blueVal;
const byte rPin = 9;
const byte gPin = 10;
const byte bPin = 11;
int first, second, third;


void setup() {
  pinMode(rPin, OUTPUT);
  pinMode(gPin, OUTPUT);
  pinMode(bPin, OUTPUT);

  Serial.begin(9600);
  Serial.flush();
  lcd.begin(16, 2);

}
void loop() {


  if (Serial.available()) {
    data = String(Serial.readString());
    first = data.indexOf(',');
    second = data.indexOf(',', first + 1);
    third = data.indexOf(',', second + 1);

    redVal = data.substring(0, first);
    blueVal = data.substring(first + 1, second);
    greenVal = data.substring(second + 1, third);

    changeColor(redVal.toInt(), greenVal.toInt(), blueVal.toInt());

    messg = data.substring(third + 1);

    lcd.clear();
    lcd.print(messg);
  }

}

void changeColor(int r, int g, int b) {
  analogWrite(rPin, r);
  analogWrite(gPin, g);
  analogWrite(bPin, b);
}
