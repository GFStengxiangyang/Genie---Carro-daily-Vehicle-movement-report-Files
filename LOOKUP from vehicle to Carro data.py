import pandas as pd
import os
import numpy as np

#Carro file
df = pd.read_excel(r"C:/Users/teng.xiangyang/Desktop/Codes and files/Carro_selected_Field.xlsx")
import datetime as dt

df['disbursement_date'] = pd.to_datetime(df['disbursement_date']).dt.date


#vehicle file
use_columns=['Vehicle No.','Tx Type.1']
df1 = pd.read_excel(r"C:/Users/teng.xiangyang/Desktop/Codes and files/Vehicle_movement_report_combined_files.xlsx",usecols = use_columns)
df1=df1.drop_duplicates(subset=["Vehicle No."], keep="first")



df2 = pd.merge(df, df1, left_on='car_plate', right_on='Vehicle No.',how = "left") 
df2 = df2.replace(np.nan, 'not in eAuto', regex=True)
import datetime as dt
today = dt.date.today()
yesterday = dt.date(today.year,today.month,today.day-1)
df2 = df2.rename(columns = {'account_status':'account_status' +  format(yesterday), 'Vehicle No.':'car_plate (eAuto)'})


output_path = "C:/Users/teng.xiangyang/Desktop/Codes and files/Master_Lookup_Files.xlsx"

df2.to_excel(output_path, index=False)


