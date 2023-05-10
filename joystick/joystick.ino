int x = 0;
int y = 0;

char send[9];

void setup() {
  Serial.begin(9600);
  pinMode(8, INPUT_PULLUP);
}

void loop() {
  x = analogRead(A0); // x좌표 읽어오기
  y = analogRead(A1); // y좌표 읽어오기
  sprintf(send, "%04d %04d", x, y); // x좌표, y좌표 형태 변환
  Serial.println(send);
  delay(100);
}