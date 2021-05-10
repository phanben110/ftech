import BEN_detectFinger as finger 
import time 
import cv2 
import math 
import pyautogui 
detectFinger = finger.handLandmarks() 

# init previous time and curent time to calculator FPS ( frame fer seconds ) 
pTime = 0 
cTime = 0 
# that is source input video 

video = "handBen2.mp4" 
video = 0

cap = cv2.VideoCapture(video) 
xBox,yBox,wBox,hBox = None,None , None,None
while True : 
    _, img = cap.read()
    img = cv2.flip(img,1)
    img1= img 
    dim = (int (2000*2/3),int ( 1100*2/3)) 
    # resize image
    #img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    detectFinger.showFinger( img1 , draw = False ) 
    pointList , box   = detectFinger.storePoint(img1 , draw= False) 
    x = 170 
    y = 50
    w = int (1920/4)  
    h = int (1080/4)  

    cv2.rectangle( img1 , (x,y) , ( w , h) , (255,255,0) ,2 )  
    if len( box ) != 0:
        xBox=box[0]-20
        yBox=box[1]-20
        wBox=box[2]+20
        hBox=box[3]+20

        cv2.rectangle( img1 , (box[0]-20, box[1]-20) , (box[2]+20 , box[3]+20 )  , (0,255,0),2 ) 

    if len(pointList) != 0: 
        
        statusFinger = detectFinger.findFingerUp( pointList ) 
        # move mount  
        if statusFinger[1]==1 and statusFinger[2]==0 and statusFinger[3]==0 and  statusFinger[4]==0: 
            if pointList[8][1] > x and pointList[8][1] < x+w and pointList[8][2] > y and pointList[8][2] < y+h : 
                cv2.circle( img1 , (pointList[8][1],pointList[8][2]) , 15, (0, 0, 255 ) , cv2.FILLED )
                xMove = ( pointList[8][1] - x ) * 4.5 
                yMove = ( pointList[8][2] - y ) * 4.5 
                pyautogui.moveTo(xMove, yMove , duration = 0 ) 
        
        # click 
        elif statusFinger[1] == 1 and statusFinger[2] ==1 and statusFinger[3]==0 and statusFinger[4] ==0: 
            if pointList[8][1] > x and pointList[8][1] < x+w and pointList[8][2] > y and pointList[8][2] < y+h : 
                cv2.circle( img1 , (pointList[8][1],pointList[8][2]) , 20 , (0, 255, 255 ) , cv2.FILLED )  
                xMove = ( pointList[8][1] - x ) * 4.5 
                yMove = ( pointList[8][2] - y ) * 4.5 
                pyautogui.click(int(xMove), int(yMove) , duration=0.3) 
                #pyautogui.dragTo(xMove, yMove , duration = 0 ) 
            #cv2.line ( img , (x1,y1) , (x2,y2) , ( 0,0,255) , 3 )  
        #cv2.circle( img , ( cx, cy ) , 15, ( 0, 255, 0) ,cv2.FILLED )  

        #length = math.hypot(x2-x1, y2-y1)  
        #print ( length )  
        img = img[yBox:yBox + hBox, xBox:wBox] 
        #cv2.imwrite("finger.png", img )  
        #cv2.imshow("image", img )  
        
    cTime = time.time() 
    fps = 1/(cTime - pTime ) 
    pTime = cTime  

    cv2.putText( img1 , str( int( fps ) ) ,(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255, 0, 255 ) ,3 ) 
    cv2.imshow("image1", img1) 
    cv2.waitKey(1) 
    img = None
    img1 = None

cv2.release 
cv2.destroyAllWindow() 

