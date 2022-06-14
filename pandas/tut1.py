import sqlite3
import pandas as pd
conn=sqlite3.connect("homes.db")
print(conn)
data=pd.read_csv("list-presidents-us-450j_0.csv")
data=pd.DataFrame(data)
data.to_csv("US_Prese.csv",index=False)
print(data)