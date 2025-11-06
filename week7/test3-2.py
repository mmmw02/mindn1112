import RPi.GPIO as GPIO
import time

PWMA = 18
AIN1 = 22
AIN2 = 27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)

motor = GPIO.PWM(PWMA, 500)
motor.start(0)

def go():
    GPIO.output(AIN1, 0)
    GPIO.output(AIN2, 1)
    motor.ChangeDutyCycle(100)

def stop():
    motor.ChangeDutyCycle(0)

# 명령어에 맞는 위치에 go(), stop() 등 함수 호출 추가
