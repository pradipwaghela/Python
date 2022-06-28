'''
#python Version: 3.10.5
#Code PAth : E:\4th_sem\INTERNSHIP\AIS140_PArsing\Ais140_To_Excel
#Log File path : E:\4th_sem\INTERNSHIP\AIS140_PArsing
'''

from csv import writer
import csv
import pandas as pd
import numpy as np

# Works fine with text file
# Need to automate file path
#file_path = "E:/4th_sem/INTERNSHIP/AIS/new_log_file/log_file.txt"

# need to resolve issues with .csv file
file_path = "E:/4th_sem/INTERNSHIP/AIS140_PArsing/Device.csv"
f = open("test.csv", 'w',newline ='\n')
w = csv.writer(f)

csv_log_path = 'E:/4th_sem/INTERNSHIP/AIS140_PArsing/Ais140_To_Excel/ais_parse_20220623/AIS140_Excel_log.csv'
excel_log_path = 'E:/4th_sem/INTERNSHIP/AIS140_PArsing/Ais140_To_Excel/ais_parse_20220623/AIS140_Excel_log.xlsx'

file = open(file_path, 'r')

s = file.read()
print(s)
lines = s.split('\n')
#print(type(lines))
filt_lines = []
for l in lines:
    if l.startswith('$'):  # return True if success
        l1 = l.replace("*", ",*,")
        single=l1.split("$")
        
        print(single)
        w.writerow(single)
"""
#df=pd.DataFrame(filt_lines)
#print(df)
#arr=np.array(df)
#print(arr.shape)
#df.to_csv("test3.csv")
        #row=[single]
        #df['no1']=[row[0][2]]
       # for i in range(len(row[0])):
        #    df.append({"no1": [row[0][i]]},ignore_index = True)
       
        #filt_lines.append(l1)
     
#print(filt_lines)
    # w.writerows([x.split(',') for x in filt_lines])

#print(filt_lines)
#array = [l.split() for l in filt_lines]
##print("\nArray:", array[::-1])

#print("\n logs:", log_df)

# And write it to csv & excel
#log_df.to_csv(csv_log_path)
#log_df.to_excel(excel_log_path)

'''
# need to implement logic to replace 'checksum*' to 'checksum,*'
for l in lines:
    if l.startswith('$'): #return True if success
        filt_lines.append(l)
        if l.startswith('*'):
            # Replace '*' with ',*'
        else:
            filt_lines.append(l)
'''
"""
print("\nFilt_Lines : ", filt_lines)

array = [l.split() for l in filt_lines]

print("\nArray:", array[::-1])


log_df = pd.DataFrame(array, columns=["Start Character", "Header", "Vendor Identification",
                                      "FW Version", "PACKET TYPE", "PACKET Status", "IMEI Number", "Vehicle Registration Number", "GPS Fix", "DDMMYYYY",
                                      "HHMMSS", "Latitude", "Latitude DIR", "Longitude", "Longitude DIR", "Speed", "Heading", "Number Of Satellites", "Altitude in meters", "PDOP",
                                      "HDOP", "Network Operator Name", "Ignition Status", "Main power status", "Main IP vtg", "Internal Battery Voltage", "Emergency Status",
                                      "Tamper Alert", "GSM Signal Strength", "MCC", "MNC", "LAC", "Cell ID",
                                      "NMR", "Ip Status", "o/p status", "frame sequence", "checksum", "End Cahracter"])

print("\n logs:", log_df)

# And write it to csv & excel
log_df.to_csv(csv_log_path)
log_df.to_excel(excel_log_path)


