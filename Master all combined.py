import pandas as pd
import os


#vehicle file
df = pd.read_excel(r"C:/Users/teng.xiangyang/Desktop/Codes and files/Vehicle_movement_report_combined_files.xlsx")

#Carro file
path = "C:/Users/teng.xiangyang/Desktop/Carro Daily/"
files = os.listdir(path)
files_xlsx = [f for f in files if f[-4:] == 'xlsx']


#Carro file
df1_list = []
for f in files_xlsx:
    df1 = pd.read_excel(os.path.join(path, f), sheet_name='floorstock_analysis')


#Master lookup files
df2 = pd.read_excel(r"C:/Users/teng.xiangyang/Desktop/Codes and files/Master_Lookup_Files.xlsx")


writer = pd.ExcelWriter(r'C:\Users\teng.xiangyang\Desktop/Codes and files\Master_Combined_Files.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='eAuto',index= False)
df1.to_excel(writer, sheet_name='Carro',index= False)
df2.to_excel(writer, sheet_name='Master_Lookup_Files',index= False)
writer.close()