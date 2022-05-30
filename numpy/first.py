"""
.reshap(size,elemnet) - Use to reshape aray
.ravel() - In normal shape
axis - Dimention of array co-odibates 
.size - total elemnt 
T :- row to column column to row
.nbytes :- Totoal byte in RAM
To create array :-
numpy.array([[]])
"""
import numpy as np
import sklearn 
def sze(aray):
    print("Size of array is ",aray.shape)
    print("Type is ",aray.dtype)
    print(aray)

myar = np.array([[10,20,30],[40,50,60],[70,80,90]])
sze(myar)

"""
print(myar[0,2])
print(myar.shape)
print(myar.dtype)
a2=np.zeros((3,3))
print(a2)
rng=np.arange(10)
sze(rng)
"""