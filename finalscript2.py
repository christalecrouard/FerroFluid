from dataclasses import field
from p2iv3 import infoGetter
import json
import sys

#COEFFICIENTS OF LINEAR REGRESSION FROM MATLAB FOR EACH RETAINING FIELDS
data_set={
  "20": {
    "height": [209.68,1.7371],
    "angle": [0.96668,0.01713],
    "module":[254.01,-0.31978],
    "centerx":[314.25,3.714],
    "centery":[269.99,1.9098]
  },
  "23": {
    "height": [215.8,2.6093],
    "angle": [1.1878,-0.011649],
    "module":[244.93,0.78557],
    "centerx":[301.94,10.52],
    "centery":[271.99,0.54085]
  },
  "26": {
    "height": [183.95,3.6709],
    "angle": [1.0345,0.035113],
    "module":[203.56,2.2197],
    "centerx":[401.55,-2.2117],
    "centery":[268.59,1.3868]
  },
  "29": {
    "height": [122.36,7.9538],
    "angle": [1.0715,0.022078],
    "module":[135.93,7.0066],
    "centerx":[484.36,-6.4736],
    "centery":[283.84,0.50769]
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

#Result of the linear function from Matlab
#Inputs : INPUT, CONSTANT, FIRST DEGREE
def matlabfn(input,cst,x1):
    output = cst + input*(x1)
    return output

#MAIN FUNCTION
def regression_main():
    args = sys.argv[1:]

    filename = args[0]
    field = int(args[1])

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
    
    a, b, c, d = infoGetter(filename)

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


    print(y_height)
    print(y_angle)
    print(y_module)
    print(y_centerx)
    print(y_centery)


    return y_height,y_angle,y_module,y_centerx,y_centery

if __name__ == '__main__':
    regression_main()