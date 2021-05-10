import BEN_detectFinger as finger 
import time 
import cv2 
import math 
detectFinger = finger.handLandmarks() 

# init previous time and curent time to calculator FPS ( frame fer seconds ) 
pTime = 0 
cTime = 0 
# that is source input video 

video = "handBen2.mp4" 
video = 0

cap = cv2.VideoCapture(video) 
count = 0 
while True : 
    _, img = cap.read() 
    img1 = img
    detectFinger.showFinger( img, draw=False ) 

    pointList , box   = detectFinger.storePoint(img , draw= False ) 

    if len( box ) != 0: 
        xBox=box[0]-20 
        yBox=box[1]-20 
        wBox=box[2]+20 
        hBox=box[3]+20
        
        #cv2.rectangle( img , (box[0]-20 , box[1]-20) , (box[2]+20 , box[3]+20 )  , (0,255,0),2 ) 

    if len(pointList) != 0: 
        
        print ( pointList[4], pointList[8] ) 
        
        x1, y1 = pointList[4][1], pointList[4][2] 
        x2, y2 = pointList[8][1], pointList[8][2] 
        cx, cy = (x1 + x2) // 2, (y1 + y2) //2 
        
        #cv2.circle( img , (x1,y1) , 15, (0, 0, 255 ) , cv2.FILLED ) 
        #cv2.circle( img , (x2,y2) , 15, (0, 0, 255 ) , cv2.FILLED ) 
        #cv2.line ( img , (x1,y1) , (x2,y2) , ( 0,0,255) , 3 )  
        #cv2.circle( img , ( cx, cy ) , 15, ( 0, 255, 0) ,cv2.FILLED )  

        #length = math.hypot(x2-x1, y2-y1)  
        #print ( length )  
       
    #fps = 1/(cTime - pTime ) 
    #pTime = cTime   
        img = img[yBox:yBox+hBox, xBox:wBox] 
        a = "data/hand" + str ( count ) +".jpg" 
        print ( "save , ", a) 
        count += 1
        cv2.imwrite(a,img ) 
    #cv2.putText( img , str( int( fps ) ) ,(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255, 0, 255 ) ,3 ) 
    cv2.imshow("image", img )  
    cv2.waitKey(1) 
cv2.release 
cv2.destroyAllWindow() 

