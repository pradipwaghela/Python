import imp
import pandas as pd
import numpy as np
import csv
from csv import writer

#Opening Files 
file_path = "Device.csv" #Log Files
file = open(file_path, 'r')

f = open("test.csv", 'w',newline ='\n') #Output CSV file 
w = csv.writer(f)

#Reading File
s = file.read()
print(s)
lines = s.split('\n')


#Writing output to test.csv file 
for l in lines:
    if l.startswith('$'):  # return True if success
        l1 = l.replace("*", ",*,")
        single=l1.split("$")
        print(single)
        w.writerow(single)