import sys
sys.path.append("/home/pi/server/static/servoCode")
from Adafruit_PWM_Servo_Driver import PWM
import os

pwm=PWM(0x40)
pwm.setPWMFreq(50)

while 1:
	try:
		tics1=input("Tics 1: ")
                tics2=input("Tics 2: ")
		pwm.setPWM(0, 0, tics1)
		pwm.setPWM(1, 0, tics2)
		print tics1
		print tics2
	except:
		print "Exception"
		pwm.setPWM(0, 0, 0)
		pwm.setPWM(1, 0, 0)
		break
