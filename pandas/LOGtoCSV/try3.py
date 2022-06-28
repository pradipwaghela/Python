import pandas as pd
import numpy as np
import csv

st1="$,1,SECURE,SAM1.0,DT,L,864337052899292,TN04E1234,0,06012080,002703,00.000000,0,00.0000000,0,000.00,000,00,0000,00.0,00.0,BSNL,1,1,15.0,0.0,0,W,00,000,000,00000,00000,0,0000,00,000161,99,*"
f=open("test2.csv","w")
w=csv.writer(f)

single=st1.split(",")
row =[single]
w.writerow(single)

#print(row)
#df = pd.DataFrame(row) 
#print(df)
#df.to_csv("test2.csv")


