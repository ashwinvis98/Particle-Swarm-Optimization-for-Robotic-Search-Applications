import os
import time
import threading
import nxt
from nxt.sensor import *

b = nxt.locator.find_one_brick('00:16:53:0C:1D:29')

def ultra():
	while True:
		distance = Ultrasonic(b, PORT_2,check_compatible=False).get_sample()

		print("obstacle at",distance)
	'''if distance < 50 :
		print('You are close Iam going to take your picture')
		filecnt = filecnt + 1
		filename = str(filecnt) + '.jpg'
		os.system('fswebcam -r 352x288 ' + filename)
		time.sleep(1)'''

def cal(i):
	i=0
	while(True):
		i=i+1
		print("i=",i)


t1=threading.Thread(target=ultra)
t2=threading.Thread(target=cal,args=1)

t1.start()
t2.start()

t1.join()
t2.join()