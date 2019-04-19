
import nxt.locator
import sys
import cv2
import cv2.aruco as aruco
from sensor.generic import * 

import tty, termios

from nxt.motor import *

b = nxt.locator.find_one_brick(host='00:16:53:0F:0F:D8')

m_left = Motor(b, PORT_C)
m_right = Motor(b, PORT_A)

light_sensor = Light(b, PORT_1, False)



both = nxt.SynchronizedMotors(m_left, m_right, 0)
rightboth = nxt.SynchronizedMotors(m_left, m_right, 50)
leftboth = nxt.SynchronizedMotors(m_right, m_left, 50)

def getch():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(fd)
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch

ch = ' '
print ("Ready")
print (b)
while ch != 'q':
	ch = getch()
	l=light_sensor.get_input_values().scaled_value
	print("light=",l)

	if ch == 'w':
		both.turn(75, 360, True)
	elif ch == 's':
		both.turn(-75, 90, True)
	elif ch == 'a':
		m_left.turn(75, 90, True)
		m_right.turn(-75, 90, True)
	elif ch == 'd':
		rightboth.turn(-75, 360, True)
	
	#aruco_fun()

	

print ("Aborted!")




