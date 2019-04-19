import nxt.locator
import threading
import sys
import cv2
import cv2.aruco as aruco
import tty, termios
from nxt.motor import *
import math
import time

xpos=10
ypos=10
alpha=10
thetha=10
xpos2=10
ypos2=10
alpha2=10
thetha2=10
xpos3=10
ypos3=10
alpha3=10
thetha3=10

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_AUTOFOCUS,0)

cap.set(3,720)
cap.set(4,720) 

a = nxt.locator.find_one_brick(host='00:16:53:11:5A:F8')
left_a = Motor(a, PORT_C)
right_a = Motor(a, PORT_A)
both_a = nxt.SynchronizedMotors(left_a, right_a, 0)
rightboth_a = nxt.SynchronizedMotors(left_a, right_a, 100)
leftboth_a = nxt.SynchronizedMotors(right_a, left_a, 100)

b = nxt.locator.find_one_brick(host='00:16:53:0F:0F:D8')
left_b = Motor(b, PORT_C)
right_b = Motor(b, PORT_A)
both_b = nxt.SynchronizedMotors(left_b, right_b, 0)
rightboth_b = nxt.SynchronizedMotors(left_b, right_b, 100)
leftboth_b = nxt.SynchronizedMotors(right_b, left_b, 100)

c = nxt.locator.find_one_brick(host='00:16:53:0C:1D:29')
left_c = Motor(c, PORT_C)
right_c = Motor(c, PORT_A)
both_c = nxt.SynchronizedMotors(left_c, right_c, 0)
rightboth_c = nxt.SynchronizedMotors(left_c, right_c, 100)
leftboth_c = nxt.SynchronizedMotors(right_c, left_c, 100)

def sign(x):
    if x<0 : return -1
    elif x>0 : return 1
    else : return 0

def navigate_a():

    #stop=0

    global xpos
    global ypos
    global alpha
    global thetha
     

    while(True):
        
        print("x=",xpos)
        print("y=",ypos)
        print("thetha=",thetha)
        print("alpha=",alpha) 
        
        delx = x-xpos
        dely = y-ypos
        dist = math.sqrt(delx*delx + dely*dely)
        angle_turn_ratio = 0.7
        distance_ratio = 0.8

        
        if (dist>=25)&(abs(thetha-alpha)>5):
        
            if abs(thetha-alpha)<=180:
                if sign(thetha-alpha)==1:
                    rightboth_a.turn(70, angle_turn_ratio*(thetha-alpha), False)
                else:
                    leftboth_a.turn(70, angle_turn_ratio*abs(thetha-alpha), False)
                            
            else:
                if sign(thetha-alpha)==1:
                    leftboth_a.turn(70, angle_turn_ratio*(360-(thetha-alpha)), False)
                else:   
                    rightboth_a.turn(70, angle_turn_ratio*(360-abs(thetha-alpha)), False)
                
        
        else:
            print("Turned!")
            if dist>=25:
                both_a.turn(67, distance_ratio*dist, False)
            else:   
                print("A reached!")
                break

def navigate_b():

    #stop=0

    global xpos2
    global ypos2
    global alpha2
    global thetha2
     

    while(True):
        
        print("x2=",xpos2)
        print("y2=",ypos2)
        print("thetha2=",thetha2)
        print("alpha2=",alpha2) 
        
        delx = x2-xpos2
        dely = y2-ypos2
        dist = math.sqrt(delx*delx + dely*dely)
        angle_turn_ratio = 0.1
        distance_ratio = 0.8

        
        if (dist>=25)&(abs(thetha2-alpha2)>5):
        
            if abs(thetha2-alpha2)<=180:
                if sign(thetha2-alpha2)==1:
                    right_b.turn(50, angle_turn_ratio*(thetha2-alpha2), False)
                    #left_b.turn(-50, angle_turn_ratio*(thetha2-alpha2), False)
                else:
                    left_b.turn(50, angle_turn_ratio*abs(thetha2-alpha2), False)
                    #right_b.turn(-50, angle_turn_ratio*abs(thetha2-alpha2), False)
        
            else:
                if sign(thetha2-alpha2)==1:
                    left_b.turn(50, angle_turn_ratio*(360-(thetha2-alpha2)), False)
                    #right_b.turn(-50, angle_turn_ratio*(360-(thetha2-alpha2)), False)
                else:   
                    right_b.turn(50, angle_turn_ratio*(360-abs(thetha2-alpha2)), False)
                    #left_b.turn(-50, angle_turn_ratio*(360-abs(thetha2-alpha2)), False)
        
        else:
            print("Turned!")
            if dist>=25:
                both_b.turn(67, distance_ratio*dist, False)
            else:   
                print("B reached!")
                break

def navigate_c():

    #stop=0

    global xpos3
    global ypos3
    global alpha3
    global thetha3
     

    while(True):
        
        print("x3=",xpos3)
        print("y3=",ypos3)
        print("thetha3=",thetha3)
        print("alpha3=",alpha3) 
        
        delx = x3-xpos3
        dely = y3-ypos3
        dist = math.sqrt(delx*delx + dely*dely)
        angle_turn_ratio = 0.1
        distance_ratio = 0.8

        
        if (dist>=25)&(abs(thetha3-alpha3)>5):
        
            if abs(thetha3-alpha3)<=180:
                if sign(thetha3-alpha3)==1:
                    right_c.turn(50, angle_turn_ratio*(thetha3-alpha3), False)
                    #left_c.turn(-50, angle_turn_ratio*(thetha3-alpha3), False)
                else:
                    left_c.turn(50, angle_turn_ratio*abs(thetha3-alpha3), False)
                    #right_c.turn(-50, angle_turn_ratio*abs(thetha3-alpha3), False)
        
            else:
                if sign(thetha3-alpha3)==1:
                    left_c.turn(50, angle_turn_ratio*(360-(thetha3-alpha3)), False)
                    #right_c.turn(-50, angle_turn_ratio*(360-(thetha3-alpha3)), False)
                else:   
                    right_c.turn(50, angle_turn_ratio*(360-abs(thetha3-alpha3)), False)
                    #left_c.turn(-50, angle_turn_ratio*(360-abs(thetha3-alpha3)), False)
        
        else:
            print("Turned!")
            if dist>=25:
                both_c.turn(67, distance_ratio*dist, False)
            else:   
                print("C reached!")
                break

def aruco_fun():
    
    global xpos
    global ypos
    global alpha
    global thetha
    global xpos2
    global ypos2
    global alpha2
    global thetha2
    global xpos3
    global ypos3
    global alpha3
    global thetha3
           
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        #print(frame.shape) #480x640
        # Our operations on the frame come here
        gray = frame#cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
        parameters =  aruco.DetectorParameters_create()
     
        #print(parameters)
     
        '''    detectMarkers(...)
            detectMarkers(image, dictionary[, corners[, ids[, parameters[, rejectedI
            mgPoints]]]]) -> corners, ids, rejectedImgPoints
            '''
            #lists of ids and the corners beloning to each id
        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
        #print(corners)
        gray = aruco.drawDetectedMarkers(gray, corners, ids)
        gray=cv2.circle(gray,((int)(x),(int)(y)),10, (0,0,255), -1)
        gray=cv2.circle(gray,((int)(x2),(int)(y2)),10, (0,255,0), -1)
        gray=cv2.circle(gray,((int)(x3),(int)(y3)),10, (255,0,0), -1)
        
        try:
            if ids[0]==1:
                ID1=0

            elif ids[1]==1:
                ID1=1

            elif ids[2]==1:
                ID1=2
                        
            if ids[0]==2:
                ID2=0

            elif ids[1]==2:
                ID2=1

            elif ids[2]==2:
                ID2=2

            if ids[0]==3:
                ID3=0

            elif ids[1]==3:
                ID3=1

            elif ids[2]==3:
                ID3=2
            

            xpos=(corners[ID1][0][0][0]+corners[ID1][0][1][0]+corners[ID1][0][2][0]+corners[ID1][0][3][0])/4
            ypos=(corners[ID1][0][0][1]+corners[ID1][0][1][1]+corners[ID1][0][2][1]+corners[ID1][0][3][1])/4
            
            xpos2=(corners[ID2][0][0][0]+corners[ID2][0][1][0]+corners[ID2][0][2][0]+corners[ID2][0][3][0])/4
            ypos2=(corners[ID2][0][0][1]+corners[ID2][0][1][1]+corners[ID2][0][2][1]+corners[ID2][0][3][1])/4

            xpos3=(corners[ID3][0][0][0]+corners[ID3][0][1][0]+corners[ID3][0][2][0]+corners[ID3][0][3][0])/4
            ypos3=(corners[ID3][0][0][1]+corners[ID3][0][1][1]+corners[ID3][0][2][1]+corners[ID3][0][3][1])/4

            gray=cv2.circle(gray,((int)(xpos),(int)(ypos)),10, (0,0,255), -1)
            gray=cv2.circle(gray,((int)(xpos2),(int)(ypos2)),10, (0,255,0), -1)
            gray=cv2.circle(gray,((int)(xpos3),(int)(ypos3)),10, (255,0,0), -1)

            if corners[ID1][0][0][1] <= corners[ID1][0][1][1]:
                        if corners[ID1][0][0][0]<=corners[ID1][0][1][0]:
                            thetha=(-math.degrees(math.atan((corners[ID1][0][0][1]-corners[ID1][0][3][1])/(corners[ID1][0][0][0]-corners[ID1][0][3][0]))))
                        else:
                            thetha=(360-math.degrees(math.atan((corners[ID1][0][0][1]-corners[ID1][0][3][1])/(corners[ID1][0][0][0]-corners[ID1][0][3][0]))))
                    
            else:
                        if corners[ID1][0][0][0] <= corners[ID1][0][1][0]:
                            thetha=(180-math.degrees(math.atan((corners[ID1][0][0][1]-corners[ID1][0][3][1])/(corners[ID1][0][0][0]-corners[ID1][0][3][0]))))
                        else: 
                            thetha=(180-math.degrees(math.atan((corners[ID1][0][0][1]-corners[ID1][0][3][1])/(corners[ID1][0][0][0]-corners[ID1][0][3][0]))))

            if xpos <= x:
                        if ypos>=y:
                            alpha=math.degrees(math.atan((ypos-y)/(x-xpos)))
                        else:
                            alpha=(360+math.degrees(math.atan((ypos-y)/(x-xpos))))
            else:
                        alpha=(180+math.degrees(math.atan((ypos-y)/(x-xpos))))  

            if corners[ID2][0][0][1] <= corners[ID2][0][1][1]:
                        if corners[ID2][0][0][0]<=corners[ID2][0][1][0]:
                            thetha2=(-math.degrees(math.atan((corners[ID2][0][0][1]-corners[ID2][0][3][1])/(corners[ID2][0][0][0]-corners[ID2][0][3][0]))))
                        else:
                            thetha2=(360-math.degrees(math.atan((corners[ID2][0][0][1]-corners[ID2][0][3][1])/(corners[ID2][0][0][0]-corners[ID2][0][3][0]))))
                    
            else:
                        if corners[ID2][0][0][0] <= corners[ID2][0][1][0]:
                            thetha2=(180-math.degrees(math.atan((corners[ID2][0][0][1]-corners[ID2][0][3][1])/(corners[ID2][0][0][0]-corners[ID2][0][3][0]))))
                        else: 
                            thetha2=(180-math.degrees(math.atan((corners[ID2][0][0][1]-corners[ID2][0][3][1])/(corners[ID2][0][0][0]-corners[ID2][0][3][0]))))

            if xpos2 <= x2:
                        if ypos2>=y2:
                            alpha2=math.degrees(math.atan((ypos2-y2)/(x2-xpos2)))
                        else:
                            alpha2=(360+math.degrees(math.atan((ypos2-y2)/(x2-xpos2))))
            else:
                        alpha2=(180+math.degrees(math.atan((ypos2-y2)/(x2-xpos2))))    

            if corners[ID3][0][0][1] <= corners[ID3][0][1][1]:
                        if corners[ID3][0][0][0]<=corners[ID3][0][1][0]:
                            thetha3=(-math.degrees(math.atan((corners[ID3][0][0][1]-corners[ID3][0][3][1])/(corners[ID3][0][0][0]-corners[ID3][0][3][0]))))
                        else:
                            thetha3=(360-math.degrees(math.atan((corners[ID3][0][0][1]-corners[ID3][0][3][1])/(corners[ID3][0][0][0]-corners[ID3][0][3][0]))))
                    
            else:
                        if corners[ID3][0][0][0] <= corners[ID3][0][1][0]:
                            thetha3=(180-math.degrees(math.atan((corners[ID3][0][0][1]-corners[ID3][0][3][1])/(corners[ID3][0][0][0]-corners[ID3][0][3][0]))))
                        else: 
                            thetha3=(180-math.degrees(math.atan((corners[ID3][0][0][1]-corners[ID3][0][3][1])/(corners[ID3][0][0][0]-corners[ID3][0][3][0]))))

            if xpos3 <= x3:
                        if ypos3>=y3:
                            alpha3=math.degrees(math.atan((ypos3-y3)/(x3-xpos3)))
                        else:
                            alpha3=(360+math.degrees(math.atan((ypos3-y3)/(x3-xpos3))))
            else:
                        alpha3=(180+math.degrees(math.atan((ypos3-y3)/(x3-xpos3))))    

            '''print("x2=",xpos2)
            print("y2=",ypos2)
            print("x3=",xpos3)
            print("y3=",ypos3)'''
            

                    #It's working.
            # my problem was that the cellphone put black all around it. The alrogithm
            # depends very much upon finding rectangular black blobs
         
                #gray = aruco.drawDetectedMarkers(gray, corners, ids)

                #print(rejectedImgPoints)
                # Display the resulting frame
                #gray=cv2.circle(gray,((int)(xpos),(int)(ypos)),10, (0,0,255), -1)
        except:
            pass 

                    
        cv2.imshow('frame',gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
     
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


#main
x = int(input("Enter x coordinate : "))
y = int(input("Enter y coordinate : "))
x2 = int(input("Enter x2 coordinate : "))
y2 = int(input("Enter y2 coordinate : "))
x3 = int(input("Enter x3 coordinate : "))
y3 = int(input("Enter y3 coordinate : "))

t1=threading.Thread(target=aruco_fun)
t2=threading.Thread(target=navigate_a)
t3=threading.Thread(target=navigate_b)
t4=threading.Thread(target=navigate_c)

t1.start()
time.sleep(6)
t2.start()
#time.sleep(5)
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()
