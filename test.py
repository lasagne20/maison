import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pin = 4 # Remplacez par le pin que vous utilisez

GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(pin, GPIO.RISING, callback=lambda x: print("Détecté!"))
print(f"Configuration réussie pour le pin {pin}")
time.sleep(30)
