from csv import writer
import csv
import pandas as pd
import numpy as np
columns=["Start Character", "Header", "Vendor Identification",
                                      "FW Version", "PACKET TYPE", "PACKET Status", "IMEI Number", "Vehicle Registration Number", "GPS Fix", "DDMMYYYY",
                                      "HHMMSS", "Latitude", "Latitude DIR", "Longitude", "Longitude DIR", "Speed", "Heading", "Number Of Satellites", "Altitude in meters", "PDOP",
                                      "HDOP", "Network Operator Name", "Ignition Status", "Main power status", "Main IP vtg", "Internal Battery Voltage", "Emergency Status",
                                      "Tamper Alert", "GSM Signal Strength", "MCC", "MNC", "LAC", "Cell ID",
                                      "NMR", "Ip Status", "o/p status", "frame sequence", "checksum", "End Cahracter"]

#opning file 
file_path = "Device.csv" # Input file
file = open(file_path,'r')
column=[]
f = open("test.csv", 'w',newline ='\n')  #Output File  
w = csv.writer(f)
w.writerow(columns) #Setting columns

s= file.read()  # Read CSV
lines = s.split('\n') 
for l in lines: 
    if l.startswith('$'): # Read row which has starting element as $
        l1 = l.replace("*", ",*,") # Seprate * from cell
        l1=l1.replace(",,","")  # Remove extra commas
        single=l1.split(",")
        for i in range(0,len(single),39):
            row=single[i:i+39]
            if(len(row)==39):
                 w.writerow(row)
            i+=39