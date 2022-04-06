import os

try:
   
    f= open("mself.txt")
    line = f.read()
    if line :
       print(line)
    else:
        print("No data in file ")
except Exception as e:
    print(e)

#print(os.listdir())