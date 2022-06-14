from dataclasses import field
from p2iv3 import infoGetter
import json
import sys

#COEFFICIENTS OF LINEAR REGRASSION FROM MATLAB FOR EACH RETAINING FIELDS
data_set={
  "20": {
    "height": [213,1.4407],
    "angle": [0.96076,0.016782],
    "module":[258.33,-0.70509],
    "centerx":[290.15,5.0805],
    "centery":[279.4,1.3811]
  },
  "23": {
    "height": [220.51,1.3358],
    "angle": [1.0656,0.021416],
    "module":[249.8,-0.53157],
    "centerx":[321.55,5.215],
    "centery":[266.76,1.9546]
  },
  "26": {
    "height": [215.93,0,68324],
    "angle": [1.085,0.029791],
    "module":[238.09,-1.0166],
    "centerx":[344.11,4.14],
    "centery":[272.49,1.6366]
  },
  "29": {
    "height": [194.83,0.31191],
    "angle": [1.0077,0.042701],
    "module":[213.1,-1.2477],
    "centerx":[357.47,4.2248],
    "centery":[281.7,1.1982]
  },
  "32": {
    "height": [195.15,1.2699],
    "angle": [0.66005,-0.015982],
    "module":[208.27,0.90643],
    "centerx":[525.06,-0.37569],
    "centery":[255.75,3.557]
  },
  "35": {
    "height": [50.269,-1.9487],
    "angle": [-0.7076,0.1568],
    "module":[54.224,-2.1559],
    "centerx":[687.22,-1.7],
    "centery":[479.97,-9.4881]
  }
}

#Result of the calibration function from Matlab
#Inputs : INPUT, CONSTANT, FIRST DEGREE
#Output : Magnetic field value
def matlabfn(input,cst,x1):
    output =  (input/x1) - (cst/x1)
    return output

def regression_main(filename, field):

    if field == 20 :
        table = data_set["20"]
    elif field == 23 :
        table = data_set["23"]
    elif field == 26 :
        table = data_set["26"]
    elif field == 29 :
        table = data_set["29"]
    elif field == 32 :
        table = data_set["32"]
    elif field == 35 :
        table = data_set["35"]
    else :
        #ERROR : VALUE NOT IN LIST OF REATAINING FIELDS
        exit("Incorrect Retaining Field Value")
    
    print("Analysis pending...")
    
    a, b, c, d = infoGetter(filename)

    if type(a)==int or len(a)==0 :
        if a==0:
            exit("No Shape Detected, Mabye the Ferrofluid is missing!")
            
    #height
    y_height = matlabfn(b,table["height"][0],table["height"][1])

    #angle
    y_angle = matlabfn(c,table["angle"][0],table["angle"][1])

    #module
    y_module = matlabfn(d,table["module"][0],table["module"][1])

    #centerx
    y_centerx = matlabfn(a[0],table["centerx"][0],table["centerx"][1])

    #centery
    y_centery = matlabfn(a[1],table["centery"][0],table["centery"][1])


    return y_height,y_angle,y_module,y_centerx,y_centery

if __name__ == '__main__':
    regression_main()