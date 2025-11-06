# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

BUZZER = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)

melody = [440]
p = GPIO.PWM(BUZZER, 100)

try:
    for freq in melody:
        p.start(50) 
        p.ChangeFrequency(freq) 
        time.sleep(0.4) 
        p.stop()
        time.sleep(0.1)
except KeyboardInterrupt:
    pass

finally:
    p.stop()
    GPIO.cleanup()

