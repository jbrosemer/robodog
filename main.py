from gpiozero import Servo
from time import sleep

servo = Servo(11)

while True:
    servo.value = 0.5