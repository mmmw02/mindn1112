# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time


BUZZER = 12
SWITCH = 5  


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)

GPIO.setup(SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

horn_freq = 440
p = GPIO.PWM(BUZZER, horn_freq)

is_buzzing = False

try:
    while True:
        switch_state = GPIO.input(SWITCH)

        if switch_state == 1 and not is_buzzing:
            p.start(50) 
            is_buzzing = True

        elif switch_state == 0 and is_buzzing:
            p.stop()  
            is_buzzing = False

        time.sleep(0.05) 

except KeyboardInterrupt:
    pass  

finally:
    p.stop()
    GPIO.cleanup()

