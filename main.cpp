#include <Servo.h>

Servo RodaE;
Servo RodaD;

const int LIMIAR_LINHA = 350;
const int PINO_SENSOR_ESQUERDO = A5;
const int PINO_SENSOR_DIREITO = A4;
const int PINO_SERVO_ESQUERDO = 5;
const int PINO_SERVO_DIREITO = 6;

void setup() {
    RodaE.attach(PINO_SERVO_ESQUERDO);
    RodaD.attach(PINO_SERVO_DIREITO);
    Serial.begin(9600);
}

void loop() {
    int SensorE = analogRead(PINO_SENSOR_ESQUERDO);
    int SensorD = analogRead(PINO_SENSOR_DIREITO);

    Serial.print("Sensor Esquerdo: ");
    Serial.println(SensorE);
    Serial.print("Sensor Direito: ");
    Serial.println(SensorD);

    if (SensorE < LIMIAR_LINHA && SensorD < LIMIAR_LINHA) { // Move em frente
        RodaE.write(0);
        RodaD.write(180);
    }
    else if (SensorE > LIMIAR_LINHA && SensorD < LIMIAR_LINHA) { // Curva à direita
        RodaE.write(0);
        RodaD.write(90);
    }
    else if (SensorE < LIMIAR_LINHA && SensorD > LIMIAR_LINHA) { // Curva à esquerda
        RodaE.write(90);
        RodaD.write(180);
    }
    else { // Para
        RodaE.write(90);
        RodaD.write(90);
    }
}