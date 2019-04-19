import nxt.locator
import threading
import sys
import cv2
import cv2.aruco as aruco
import tty, termios
from nxt.motor import *
import math
import time
import random
import nxt
from nxt.sensor import *

p=400
q=200

x=0
y=0
x2=0
y2=0
x3=0
y3=0

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

global_best_cost=1000000.00
global_best_x=0.00
global_best_y=0.00
best_cost1=1000000.00
best_x1=0
best_y1=0
best_cost2=1000000.00
best_x2=0
best_y2=0
best_cost3=1000000.00
best_x3=0
best_y3=0

velx=0
vely=0
velx2=0
vely2=0
velx3=0
vely3=0

a_reached=1
b_reached=1
c_reached=1
#all_reached=0

lab=0
lbc=0
lca=0

stop=0

cap = cv2.VideoCapture(1) 

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

def distance():

	lab = math.sqrt((xpos-xpos2)*(xpos-xpos2)+(ypos-ypos2)*(ypos-ypos2))
	lbc = math.sqrt((xpos2-xpos3)*(xpos2-xpos3)+(ypos2-ypos3)*(ypos2-ypos3))
	lca = math.sqrt((xpos3-xpos)*(xpos3-xpos)+(ypos3-ypos)*(ypos3-ypos))

def obstacle_detect_a():

    global a

    #while(True):
    print("a")
    distance_a = Ultrasonic(a, PORT_2,check_compatible=False).get_sample()
    time.sleep(2)
    if distance_a<=10:
        print("A detected obstacle, ",distance_a)
        leftboth_a.turn(70,180,False)
        both_a.turn(67,360,False)
        
def obstacle_detect_b():

    global b

    while(True):
    	print("b")
    distance_b = Ultrasonic(b, PORT_2,check_compatible=False).get_sample()
    
    if distance_b<=10:
        print("B detected obstacle, ",distance_b)
        left_b.turn(-50,270,False)
        both_b.turn(67,500,False)

def obstacle_detect_c():

    global c

    while(True):
	    print("c")
    distance_c = Ultrasonic(c, PORT_2,check_compatible=False).get_sample()
    
    if distance_c<=10:
        print("C detected obstacle, ",distance_c)
        left_c.turn(-50,270,False)
        both_c.turn(67,500,False)


def vector_field(x,y):
     
    global p
    global q
    cost=(x-p)*(x-p)+(y-q)*(y-q)
    return cost

def check_all_reached():

    global xpos
    global ypos
    global xpos2
    global ypos2
    global xpos3
    global ypos3
    #global all_reached
    
    s1=math.sqrt((xpos-xpos2)*(xpos-xpos2)+(ypos-ypos2)*(ypos-ypos2))
    s2=math.sqrt((xpos2-xpos3)*(xpos2-xpos3)+(ypos2-ypos3)*(ypos2-ypos3))
    s3=math.sqrt((xpos3-xpos)*(xpos3-xpos)+(ypos3-ypos)*(ypos3-ypos))
    print("sum of sides",s1+s2+s3)

    if (s1+s2+s3)<270:
        print("Mission Complete")
        return 1
      
    else:   
        return 0


def pso():
    
    global x
    global y
    global x2
    global y2
    global x3
    global y3

    global xpos
    global ypos
    global xpos2
    global ypos2
    global xpos3
    global ypos3
    
    global global_best_cost
    global global_best_x
    global global_best_y
    global best_cost1
    global best_x1
    global best_y1
    global best_cost2
    global best_x2
    global best_y2
    global best_cost3
    global best_x3
    global best_y3

    global velx
    global vely
    global velx2
    global vely2
    global velx3
    global vely3

    global a_reached
    global b_reached
    global c_reached

    distance()

    w = 0.7298
    wdamp = 0.95
    c1 = 1.4962
    c2 = 1.4962
    maxvel = 0.2*400
    minvel = -maxvel

    print("PSO")

    if vector_field(x,y) < best_cost1:
        best_cost1=vector_field(x,y)
        best_x1=x
        best_y1=y

    if vector_field(x2,y2) < best_cost2:
        best_cost2=vector_field(x2,y2)
        best_x2=x2
        best_y2=y2

    if vector_field(x3,y3) < best_cost3:
        best_cost3=vector_field(x3,y3)
        best_x3=x3
        best_y3=y3

    if (best_cost1<=best_cost2)&(best_cost1<=best_cost3)&(best_cost1<=global_best_cost):
        global_best_cost=best_cost1
        global_best_x=x
        global_best_y=y

    elif (best_cost2<=best_cost1)&(best_cost2<=best_cost3)&(best_cost2<=global_best_cost):
        global_best_cost=best_cost2
        global_best_x=x2
        global_best_y=y2

    else:
        global_best_cost=best_cost3
        global_best_x=x3
        global_best_y=y3


    velx = w*velx + c1*(best_x1-x) + c2*(global_best_x-x)
    vely = w*vely + c1*(best_y1-y) + c2*(global_best_y-y)

    velx2 = w*velx2 + c1*(best_x2-x2) + c2*(global_best_x-x2)
    vely2 = w*vely2 + c1*(best_y2-y2) + c2*(global_best_y-y2)

    velx3 = w*velx3 + c1*(best_x3-x3) + c2*(global_best_x-x3)
    vely3 = w*vely3 + c1*(best_y3-y3) + c2*(global_best_y-y3)

    velx = max(velx,minvel)
    velx = min(velx,maxvel)
    velx2 = max(velx2,minvel)
    velx2 = min(velx2,maxvel)
    velx3 = max(velx3,minvel)
    velx3 = min(velx3,maxvel)

    x = x + velx
    y = y + vely
    x2 = x2 + velx2
    y2 = y2 + vely2
    x3 = x3 + velx3
    y3 = y3 + vely3

    x = max(x,50)
    x = min(x,590)
    y = max(y,50)
    y = min(y,430)
            
    x2 = max(x2,50)
    x2 = min(x2,590)
    y2 = max(y2,50)
    y2 = min(y2,430)
            
    x3 = max(x3,50)
    x3 = min(x3,590)
    y3 = max(y3,50)
    y3 = min(y3,430)

	
    w = w* wdamp

    
    a_reached = 0
    b_reached = 0
    c_reached = 0

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
    global a_reached
    global lab
    global lca
     

    
    while(True):
        
        '''print("x=",xpos)
        print("y=",ypos)
        print("thetha=",thetha)
        print("alpha=",alpha)''' 
        
        delx = x-xpos
        dely = y-ypos
        dist = math.sqrt(delx*delx + dely*dely)
        angle_turn_ratio = 0.7
        distance_ratio = 0.8
        if (lab  < 150)|(lca < 150):
        	obstacle_detect_a()


        if (dist>=40)&(abs(thetha-alpha)>7):
        
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
      
            #obstacle_detect_a()    
        
       	else:
            #print("Turned!")
            if dist>=40:
                both_a.turn(67, distance_ratio*dist, False)
                #obstacle_detect_a()

            else:   
                print("A reached!")
                a_reached=1
                if check_all_reached()==1:
                	break
		
        if dist<30:
            obstacle_detect_a()

def navigate_b():

    #stop=0

    global xpos2
    global ypos2
    global alpha2
    global thetha2
    global b_reached
    global lab
    global lbc
     

    while(True):
        
        '''print("x2=",xpos2)
        print("y2=",ypos2)
        print("thetha2=",thetha2)
        print("alpha2=",alpha2)''' 
        
        delx = x2-xpos2
        dely = y2-ypos2
        dist = math.sqrt(delx*delx + dely*dely)
        angle_turn_ratio = 0.1
        distance_ratio = 0.8
        if (lbc  < 150)|(lab < 150):
        	obstacle_detect_b()
        
        if (dist>=40)&(abs(thetha2-alpha2)>5):
        
            if abs(thetha2-alpha2)<=180:
                if sign(thetha2-alpha2)==1:
                    right_b.turn(50, angle_turn_ratio*(thetha2-alpha2), False)
                else:
                    left_b.turn(50, angle_turn_ratio*abs(thetha2-alpha2), False)
        
            else:
                if sign(thetha2-alpha2)==1:
                    left_b.turn(50, angle_turn_ratio*(360-(thetha2-alpha2)), False)
                else:   
                    right_b.turn(50, angle_turn_ratio*(360-abs(thetha2-alpha2)), False)
        
        else:
            #print("Turned!")
            if dist>=40:
                both_b.turn(67, distance_ratio*dist, False)
            else:   
                print("B reached!")
                b_reached=1
                if check_all_reached()==1:
                    break
        

                

def navigate_c():

    #stop=0

    global xpos3
    global ypos3
    global alpha3
    global thetha3
    global c_reached
    global lbc
    global lca

    while(True):
        
        '''print("x3=",xpos3)
        print("y3=",ypos3)
        print("thetha3=",thetha3)
        print("alpha3=",alpha3)''' 
        
        delx = x3-xpos3
        dely = y3-ypos3
        dist = math.sqrt(delx*delx + dely*dely)
        angle_turn_ratio = 0.1
        distance_ratio = 0.8
        if (lbc  < 150)|(lca < 150):
        	obstacle_detect_c()

               
        if (dist>=40)&(abs(thetha3-alpha3)>5):
        
            if abs(thetha3-alpha3)<=180:
                if sign(thetha3-alpha3)==1:
                    right_c.turn(50, angle_turn_ratio*(thetha3-alpha3), False)
                else:
                    left_c.turn(50, angle_turn_ratio*abs(thetha3-alpha3), False)
        
            else:
                if sign(thetha3-alpha3)==1:
                    left_c.turn(50, angle_turn_ratio*(360-(thetha3-alpha3)), False)
                else:   
                    right_c.turn(50, angle_turn_ratio*(360-abs(thetha3-alpha3)), False)
        
        else:
            #print("Turned!")
            if dist>=40:
                both_c.turn(67, distance_ratio*dist, False)
            else:   
                print("C reached!")
                c_reached=1
                if check_all_reached()==1:
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
    global p
    global q
           
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
        gray=cv2.circle(gray,((int)(p),(int)(q)),10, (255,255,255), -1)
        
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

        if (a_reached==1)&(b_reached==1)&(c_reached==1):
            pso()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


#main

t1=threading.Thread(target=aruco_fun)
t2=threading.Thread(target=navigate_a)
t3=threading.Thread(target=navigate_b)
t4=threading.Thread(target=navigate_c)
#t7=threading.Thread(target=obstacle_detect_a)
#t8=threading.Thread(target=obstacle_detect_b)
#t9=threading.Thread(target=obstacle_detect_c)

t1.start()
time.sleep(5)

x=xpos
y=ypos
x2=xpos2
y2=ypos2
x3=xpos3
y3=ypos3

t2.start()
t3.start()
t4.start()
#t7.start()
#t8.start()
#t9.start()

t2.join()
t3.join()
t4.join()

t1.join()
#t7.join() 
#t8.join()
#t9.join()