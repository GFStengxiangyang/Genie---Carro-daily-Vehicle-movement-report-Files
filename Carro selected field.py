import pandas as pd
import os
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


output_path = "C:/Users/teng.xiangyang/Desktop/Codes and files/Carro_selected_Field.xlsx"
df.to_excel(output_path, index=False)

