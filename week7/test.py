# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

sw_pins = [5, 6, 13, 19]

sw_old_values = [0] * len(sw_pins)

click_counts = [0] * len(sw_pins)

# GPIO settings
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for pin in sw_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        for i in range(len(sw_pins)):
            current_value = GPIO.input(sw_pins[i])

            if current_value == 1 and sw_old_values[i] == 0:
                click_counts[i] += 1

                print("('SW{0} click', {1})".format(i + 1, click_counts[i]))

            sw_old_values[i] = current_value

except KeyboardInterrupt:
    print("\nProgram terminated by user.")
finally:
    GPIO.cleanup()
