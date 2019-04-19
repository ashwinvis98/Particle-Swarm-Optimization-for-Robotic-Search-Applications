import os
import time
import threading
import nxt
from nxt.sensor import *

b = nxt.locator.find_one_brick('00:16:53:0C:1D:29')

while True:

	intensity = Light(b, PORT_1,illuminated=False).get_sample()
	
	print(intensity)