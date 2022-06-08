import csv
from distutils.log import info
from p2iv3 import infoGetter
import os.path
from MagneticFieldValues import constant, mag1, mag2



def main():

    f = open('data_20.csv','w')
    writer = csv.writer(f)

    # write  header of the csv file
    header = ['centroidx','centroidy','height','angle','module','mag_field']
    writer.writerow(header)

    files_dir = "./Gdefinite7/"
    #list files
    directory = os.listdir(files_dir)
    for files in directory:
        fs = files.split(".")
        if fs[1] == "jpg":
            add_data(files, files_dir, writer)

    # close the file
    f.close()

def getMagField(fullstring):
    field = 0
    lin = 0
    col = 0

    for ind1 in mag1 : 
        
        if  str(ind1) in fullstring[3:5]:
            lin = mag1.index(ind1)
        else :
            continue
    for ind2 in mag2:
        
        if  str(ind2) in fullstring[6:8]:
            col = mag2.index(ind2)
        else :
            continue
    field = constant[lin][col]

    return field

def add_data(filename, dir, wri):
    #print(dir+filename)
    a, b, c, d = infoGetter(dir+filename)
    if b != 0:
        e = getMagField(filename)

        data = [a[0], a[1], b,c,d,e]
        wri.writerow(data)


if __name__ == '__main__':
    main()
