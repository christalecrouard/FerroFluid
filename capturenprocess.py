from finalscript3 import regression_main
import capturefn
import sys

def main():
    
    args = sys.argv[1:]
    filename = args[0]
    file = capturefn.capture(filename)
    
    field = int(args[1])
    
    output = regression_main(file,field)
    
    out=[]
    for index in range(len(output)):
        out.append(((output[index]-0.5)/0.003125)-640)
    print(out)
    
    
if __name__ == '__main__':
    main()
    