/*
コンテンツ工学システム11班
Ver. 0.0 (2025/6/28)



コード説明
const uint8_t
  -> 8ピット整数；intよりメモリを節約できる
inline int [関数名] (){
  -> 一度しか呼び出さない関数の定義にinlineを使うと速くなる
  int なら整数を，boolなら真偽を返す（return 結果;）．boolは何も返さない．


*/
#include <Servo.h>

Servo servo;

//analog
const uint8_t PhotocellPin = 0; //brightness sensor
const uint8_t MicPin = 1; //microphone

//digital
const uint8_t ServoPin = 8; //Servo moter
const uint8_t BuzzerPin = 9; //Buzzer

int Brightness = 0;
int Volume = 0;

bool sleep = false;
uint16_t t = 0;

float goToBed = 23.0;
const uint32_t baudRate = 115200; 

void setup() {
  servo.attach(ServoPin);
  Serial.begin(baudRate);
  sleep = true;
}

void loop() {
  Brightness = analogRead(PhotocellPin);
  Volume = analogRead(MicPin);

  if (presentTime() == goToBed){
    sleep = true;
    t = 0;
  }
  if (ifBright && sleep == true){
    if (t==0){
      t=1;
    }
    Serial.println("warning"); //processingでこのシグナルを受け取ったら警告を鳴らす
    if (ifReacted() && t <= 5000){ // 5000カウントの間起きてるか調べる
      sleep = false;
    }
    if (t > 5000){
      SwitchOff();
    }
    t++;
  }
}


float presentTime(){ //時刻を取得；23時30分なら 「23.5」を返す．時

}


//loopの中に組み込んじゃってもいいよ
inline bool ifBright(){ //明るくて，時間が遅ければTrueを，そうでなければFalseを返す．
  return true;
}

inline bool ifReacted(){ //警告後，叫んだのを検知したらTrueを，そうでなければFalseを返す．
  return true;
}

//loopの中に組み込んじゃってもいいよ
inline void SwitchOff(){ //証明のスイッチを切る（スイッチを押したらサーボモーターはもとの状態に戻る）
  
}
