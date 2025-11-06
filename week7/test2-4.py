# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

BUZZER = 12
SW1, SW2, SW3, SW4 = 5, 6, 13, 19
sw_pins = [SW1, SW2, SW3, SW4]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)
for pin in sw_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

p = GPIO.PWM(BUZZER, 100)

melody1 = [261, 261, 392, 392, 440, 440, 392, 349, 349, 330, 330, 294, 294, 262]
beats1 =  [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2]

melody2 = [261, 261, 261, 261, 261, 330, 392, 392, 330, 261, 392, 392, 330]
beats2 =  [2, 1, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 2]

melody3 = [330, 294, 261, 294, 330, 330, 330, 294, 294, 330, 294, 261]
beats3 =  [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1]

melody4 = [494, 494, 440, 349, 392, 349]
beats4 =  [1, 1, 2, 1, 1, 2]

songs = [melody1, melody2, melody3, melody4]
song_beats = [beats1, beats2, beats3, beats4]
song_names = ["Twinkle Twinkle Little Star", "The Bear Family", "Airplane", "Happy Birthday"]

sw_old_vals = [0, 0, 0, 0]

def play_song(melody, beats):
    base_time = 0.5
    for i in range(len(melody)):
        p.start(50)
        p.ChangeFrequency(melody[i])
        time.sleep(beats[i] * base_time)
        p.stop()
        time.sleep(0.05)

try:
    while True:
        sw_current_vals = [GPIO.input(pin) for pin in sw_pins]

        for i in range(len(sw_pins)):
            if sw_current_vals[i] == 1 and sw_old_vals[i] == 0:
                print("SW{} Play: {}".format(i + 1, song_names[i]))
                play_song(songs[i], song_beats[i])

        sw_old_vals = sw_current_vals
        time.sleep(0.05)

except KeyboardInterrupt:
    pass

finally:
    p.stop()
    GPIO.cleanup()

