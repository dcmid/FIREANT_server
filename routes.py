from flask import Flask, render_template
import sys
sys.path.append("/home/pi/server/static/servoCode")
from Adafruit_PWM_Servo_Driver import PWM
import os
app = Flask(__name__)

pwm=PWM(0x40)
pwm.setPWMFreq(50)

left=0
right=1

def motorsForward():
	print "FORWARD"
	pwm.setPWM(0, 0, 400)
	pwm.setPWM(1, 0, 400)

def motorsLeft():
	print "LEFT"
	pwm.setPWM(0, 0, 265)
	pwm.setPWM(1, 0, 400)

def motorsReverse():
	print "REVERSE"
	pwm.setPWM(0, 0, 265)
	pwm.setPWM(1, 0, 265)

def motorsRight():
	print "RIGHT"
	pwm.setPWM(0, 0, 400)
	pwm.setPWM(1, 0, 265)
	
def motorsStop():
	print "STOP"
	pwm.setPWM(0, 0, 335)
	pwm.setPWM(1, 0, 335)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/forward')
def forward():
	motorsForward()
	return 'Drivin'

@app.route('/left')
def left():
	motorsLeft()
	return 'Drivin'

@app.route('/backward')
def backward():
	motorsReverse()
	return 'Drivin'

@app.route('/right')
def right():
	motorsRight()
	return 'Drivin'

@app.route('/stop')
def stop():
	motorsStop()
	return 'Drivin'

@app.route('/shutdown')
def shutdown():
	os.system("shutdown -h now")

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
