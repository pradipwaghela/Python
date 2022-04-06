"""
open("Filename","Mode")
                    r - read only
                    w - Write only
                    x - Create if does not exists 
                    a - Add content to file 
                    t - text mode default
                    b - Binary mode
                    + - Read + Write

"""                 
import os

def ReadFile():
    try:
        f= open("mself.txt", "r")
        line = f.read()
        if line :
            print(line)
        else:
            print("No data in file ")
    except Exception as e:
        print(e)
def WriteFile(conte):
    try:
        f= open("mself.txt", "a")
        f.write(conte)
    except Exception as e:
        print(e)

conte=input("Wrtite To file")
WriteFile(conte)
ReadFile()