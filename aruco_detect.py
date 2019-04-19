import cv2
import cv2.aruco as aruco
 
cap = cv2.VideoCapture(1)
'''cap.set(cv2.CAP_PROP_AUTOFOCUS,0)

cap.set(3,720)
cap.set(4,720)'''

i=0
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


    cv2.imshow('frame',gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
    	break 
    
    i=i+1


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()