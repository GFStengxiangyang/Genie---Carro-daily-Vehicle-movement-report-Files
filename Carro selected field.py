import pandas as pd
import os
import numpy as np
#Carro file
path = "C:/Users/teng.xiangyang/Desktop/Carro Daily/"
files = os.listdir(path)
files_xlsx = [f for f in files if f[-4:] == 'xlsx']
use_columns=['group_id','group_name','car_plate','account_status','disbursement_date','chassis_number']


#Carro file
df_list = []
for f in files_xlsx:
    df = pd.read_excel(os.path.join(path, f), sheet_name='floorstock_analysis', usecols = use_columns)

import datetime as dt

df['disbursement_date'] = pd.to_datetime(df['disbursement_date']).dt.date

#Change the date if needed

date1 =dt.date(2023, 1, 1)
df = df.drop(df[(df['account_status'] == 'Settled') & (df['disbursement_date'] < date1)].index)

#Problematic dealer

df1= pd.read_excel(r"C:/Users/teng.xiangyang/Desktop/Problematic/Problematic Dealer.xlsx")

df2= pd.merge(df, df1, left_on='group_id', right_on='Group ID',how = "left") 

output_path = "C:/Users/teng.xiangyang/Desktop/Codes and files/Carro_selected_Field.xlsx"
df2.to_excel(output_path, index=False)

