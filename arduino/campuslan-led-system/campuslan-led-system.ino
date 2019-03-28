#define MAX_INTENSITY 1024/4
#define MIN_INTENSITY
#define DELAYTIME 3000

// LED type
#define RGB_COMMON_ANODE

// LED pins
#define LEDRED A0
#define LEDGRN A1
#define LEDBLU A5

// PWM setup. For normal Arduinos, this is just used for maths
#define PWMFREQ 1000
#define PWMBITS 10
#define PWMMAXV ((1<<PWMBITS)-1)

#if defined(ARDUINO_ARCH_ESP32)
#define ESP32_QUIRKS_NO_ANALOGWRITE
#endif

// Based on https://raw.githubusercontent.com/espressif/arduino-esp32/master/libraries/ESP32/examples/AnalogOut/ledcWrite_RGB/ledcWrite_RGB.ino

// Platform-dependent code to initialize LED
void configLED()
{
  #ifdef ESP32_QUIRKS_NO_ANALOGWRITE
    Serial.println("Doing ESP32 setup");
    ledcAttachPin(LEDRED, 1); // assign RGB led pins to channels
    ledcAttachPin(LEDGRN, 2);
    ledcAttachPin(LEDBLU, 3);
    // Initialize channels 
    // channels 0-15, resolution 1-16 bits, freq limits depend on resolution
    // ledcSetup(uint8_t channel, uint32_t freq, uint8_t resolution_bits);
    ledcSetup(1, PWMFREQ, PWMBITS); // PWMFREQ Hz PWM, PWMBITS resolution
    ledcSetup(2, PWMFREQ, PWMBITS);
    ledcSetup(3, PWMFREQ, PWMBITS);
  #else
    Serial.println("Doing non-ESP32 setup");
    pinMode(LEDRED, OUTPUT);
    pinMode(LEDGRN, OUTPUT);
    pinMode(LEDBLU, OUTPUT);
  #endif
}

// Platform-dependent code to set the value of a color (analogWrite vs ledcWrite)
void setColorValue(byte color, int value)
{
  Serial.print("Setting color ");
  Serial.print(color);
  Serial.print(" to ");
  Serial.println(floor(value));//*/
  #ifdef RGB_COMMON_ANODE
  value = PWMMAXV - value;
  #endif
  #ifdef ESP32_QUIRKS_NO_ANALOGWRITE
    ledcWrite(color, value);
  #else
    if(color == 1) analogWrite(LEDRED, value);
    else if(color == 2) analogWrite(LEDGRN, value);
    else if(color == 3) analogWrite(LEDBLU, value);
  #endif
}
void setColor(float R, float G, float B)
{
  Serial.print(R);
  Serial.print(" ");
  Serial.print(G);
  Serial.print(" ");
  Serial.println(B);
  // Simplified intensity calculation (meant to limit total output)
  if(R + G + B > MAX_INTENSITY) {
    Serial.println("Scaling intensity");
    float intensityScalingFactor = MAX_INTENSITY / (R + G + B);
    R = R * intensityScalingFactor;
    G = G * intensityScalingFactor;
    B = B * intensityScalingFactor;
    Serial.print(R);
    Serial.print(" ");
    Serial.print(G);
    Serial.print(" ");
    Serial.println(B);
  }//*/
  setColorValue(1, R);
  setColorValue(2, G);
  setColorValue(3, B);
}

// the setup routine runs once when you press reset:
void setup() 
{            
  Serial.begin(115200);
  delay(10); 
  configLED();
}

// void loop runs over and over again
void loop() 
{
  setColor(PWMMAXV, 0, 0);
  delay(DELAYTIME);
  setColor(0, PWMMAXV, 0);
  delay(DELAYTIME);
  setColor(0, 0, PWMMAXV);
  delay(DELAYTIME);
  setColor(PWMMAXV, PWMMAXV, PWMMAXV);
  delay(DELAYTIME);
  setColor(0, 0, 0);
  delay(DELAYTIME);
}
