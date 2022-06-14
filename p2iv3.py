from email import iterators
from operator import mod
import cv2
import numpy as np

#DEFINITIONS OF FUNCTIONS
def nothing(x):
    pass
   
def listX (contour):
    coord = []
    for i in range(len(contour)):
        coord.append(contour[i][0][0])
    return coord

def listY (contour):
    coord = []
    for i in range(len(contour)):
        coord.append(contour[i][0][1])
    return coord

def findTop1(contour, ly):
    return ly.index(min(ly))

def findBottom1(contour, ly):
    return ly.index(max(ly))

def findLeft(contour, lx):
    return lx.index(min(lx))

def findRight(contour, lx):
    return lx.index(max(lx))

def findInfo(tp, bp, lp, rp, lx, ly):
    #milieu
    mid = int((lx[lp]+lx[rp])/2)
    #hauteur
    height = ly[bp]-ly[tp]
    #angle
    a = (mid-lx[tp])
    b = (height)
    if a!=0 :
        angle = np.arctan(b/a)
    else:
        angle = 0
    #module
    mod = np.sqrt((height*height)+(mid-lx[tp])*(mid-lx[tp]))

    return height, angle, mod

def checkColor(bound, img):
    for (low, upp) in bound :
        low = np.array(low, dtype ='uint8')
        upp = np.array(upp, dtype ='uint8')
        
        mask = cv2.inRange(img, low, upp)
        outp = cv2.bitwise_and(img, img, mask = mask)
        
        black_out = cv2.imwrite("black.jpg",mask)
        
        return mask
    
def infoGetter(filename):

    centres = []
    heights = []
    angles = []
    modules = []
    
    boundaries = [([0,0,0],[100,100,100])]
    
    frame = cv2.imread(filename)
    #imgCropped = frame[1900:3080,900:1510]
    imgCropped = frame[1000:5000,800:5000]
    frame = cv2.resize(imgCropped,(1000,500))
    
    cv2.imwrite("imgcrop.jpg",frame)
    
    
    
    bl_out = checkColor(boundaries, frame)
    areabl = []
    contours_check, hierarchy = cv2.findContours(bl_out,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours_check:
        area_check = cv2.contourArea(contour)
        areabl.append(area_check)
    cv2.imwrite("imgcheck.jpg",bl_out)
    if all(v < 100 for v in areabl) :
        exit("No fluid detected")
            
    
    
    
    
    ret,thresh1 = cv2.threshold(frame,127,255,cv2.THRESH_BINARY_INV)

    ## parameters selection
    l_h = 14
    l_s = 16
    l_v = 15
    u_h = 170
    u_s = 255
    u_v = 255
    N_erode = 4
    eps = 2/100
    area_min = 100
    area_max = 1800
    N_erode = N_erode if N_erode>0 else 1

    imgGray = cv2.cvtColor(thresh1,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
    imgCanny = cv2.Canny(imgBlur,50,50)

    height=0
    angle=0
    module=0
    p=0

    ## find contours in image based on color mask
    contours, hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, eps*perimeter, True)
        x,y,w,h = cv2.boundingRect(contour)
        
        if (area_min < area) and (2<len(approx)):
            
            x_0 = int(x+w/2)
            y_0 = int(y+h/2)
            frame = cv2.putText(frame, str(len(approx)), (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), thickness=1)
            frame = cv2.circle(frame, (x_0, y_0), 10, (255,255,50), -1)
            cv2.drawContours(thresh1, contour, -1, (255, 0, 0), 3)

            #Bounding Rectangle
            #peri = cv2.arcLength(contour,True)
            #approx = cv2.approxPolyDP(contour,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(thresh1,(x,y),(x+w,y+h),(0,255,0),2)

            #Some calculations
            
            if cv2.contourArea(contour) < 160:
                nothing
            else:

                #Centroid or Center of Mass
                M = cv2.moments(contours[p])
                centres.append((int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])))

                #LIST OF CONTOUR POINTS
                Xaxis = listX(contours[p])
                Yaxis = listY(contours[p])

                top = findTop1(contours[p], Yaxis)
                bottom = findBottom1(contours[p], Yaxis)
                left = findLeft(contours[p], Xaxis)
                right = findRight(contours[p], Xaxis)
                
                height, angle , module = findInfo(top, bottom, left, right, Xaxis, Yaxis)
                heights.append(height)
                angles.append(angle)
                modules.append(module)
                #PRINT HEIGHT ANGLE AND MODULE
                #print(height,angle,module)
        p += 1
        
    if len(centres) <= 1:
        centres.append(0)
        heights.append(0)
        angles.append(0)
        modules.append(0)
    if len(centres) == 1:
        centres.append(0)
        heights.append(0)
        angles.append(0)
        modules.append(0)

    return centres[0], heights[0], angles[0], modules[0]

