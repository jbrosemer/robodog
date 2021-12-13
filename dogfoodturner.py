from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
start = 0
try:
    while True:
        servonum = input("enter which pin the servo is attached to on the hat: ")
        angle = input("enter the motor speed: ")
        kit.servo[servonum].angle = (int(angle))
        print('turning')
except KeyboardInterrupt:
    for i in range(16):
        kit.servo[i].angle = 90
    print('keyboard interrupt pressed')