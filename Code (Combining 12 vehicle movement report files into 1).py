import pandas as pd
import os
from natsort import natsorted 

path = "C:/Users/teng.xiangyang/Desktop/Vehicle movement report/"
files = os.listdir(path)
files_xlsx = [f for f in files if f[-4:] == 'xlsx']
files_xlsx = natsorted(files_xlsx)

df_list = []
for f in files_xlsx:
    data = pd.read_excel(os.path.join(path, f),skiprows=4)
    df_list.append(data)
 
df = pd.concat(df_list)

df['Chassis No'] = df['Chassis No'].str.replace('-','')


output_path = "C:/Users/teng.xiangyang/Desktop/Codes and files/Vehicle_movement_report_combined_files.xlsx"
df.to_excel(output_path, index=False)

