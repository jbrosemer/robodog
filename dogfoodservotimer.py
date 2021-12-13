from adafruit_servokit import ServoKit
import time
kit = ServoKit(channels=16)
#servonum = position on the hat, angle is distance from 90
# <90 CW            >90 CCW
#timer is how long the servo should spin
def turnservo(servonum, angle, timer):
    start = time.time()
    while time.time()-start > timer:
        kit.servo[servonum].angle = (int(angle))
        print('turning')
    #reset servo to stop 90 should be stop with the continuous servo
    kit.servo[servonum].angle = 90