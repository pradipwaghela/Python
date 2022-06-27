
print ("Always executed")
 

def thisi():
    print("Inside Function")



if __name__ == "__main__":
    print ("Executed when invoked directly")
    thisi()
else:
    print ("Executed when imported")
