import pandas as pd
import os
import numpy as np

#Carro file
df = pd.read_excel(r"C:/Users/teng.xiangyang/Desktop/Codes and files/Carro_selected_Field.xlsx")
import datetime as dt

df['disbursement_date'] = pd.to_datetime(df['disbursement_date']).dt.date
df['car_plate'] = df['car_plate'].str.upper()
df['chassis_number'] = df['chassis_number'].str.upper()



#vehicle file (by vehicle No. look up)
use_columns=['Vehicle No.','Tx Type.1']
df1 = pd.read_excel(r"C:/Users/teng.xiangyang/Desktop/Codes and files/Vehicle_movement_report_combined_files.xlsx",usecols = use_columns)
df1=df1.drop_duplicates(subset=["Vehicle No."], keep="first")
df1['Vehicle No.'] = df1['Vehicle No.'].str.upper()


#vehicle file (by chassis no look up)
use_columns=['Chassis No','Tx Type.1']
df2 = pd.read_excel(r"C:/Users/teng.xiangyang/Desktop/Codes and files/Vehicle_movement_report_combined_files.xlsx",usecols = use_columns)
df2=df2.drop_duplicates(subset=["Chassis No"], keep="first")
df2['Chassis No'] = df2['Chassis No'].str.upper()







df3 = pd.merge(df, df1, left_on='car_plate', right_on='Vehicle No.',how = "left") 
df4 = pd.merge(df3, df2, left_on='chassis_number', right_on='Chassis No',how = "left") 

df4 = df4.replace(np.nan, 'not in eAuto', regex=True)
import datetime as dt
today = dt.date.today()
yesterday = today - dt.timedelta(days=1)
df4 = df4.rename(columns = {'account_status':'account_status' +  format(yesterday), 'Vehicle No.':'car_plate (eAuto)', 'Chassis No':'Chassis (eAuto)'})


output_path = "C:/Users/teng.xiangyang/Desktop/Codes and files/Master_Lookup_Files.xlsx"

df4.to_excel(output_path, index=False)


