import pandas as pd

#The File needs to have a table

# Note Error need to install -> pip install --force-reinstall -v "openpyxl==3.1.0" 


#Need to define the file and the TableName
excel_data = pd.read_excel('example.xlsx')
TableName = 'schema.table'

# Read the values of the file in the dataframe
data = pd.DataFrame(excel_data).fillna('') 
# check with format

columnQuery = "INSERT INTO " + TableName + " ( "
frist = True

#Mapping columns of the dataframe
for col_names in data.columns:
    if(frist):
        columnQuery = columnQuery + col_names
        frist = False
    else:
        columnQuery = columnQuery + ',' + col_names

#Values
columnQuery = columnQuery + ") VALUES ( "  

list_columns = list(data.columns)

ArrayFinalInsert = []
dict_p = data.to_dict(orient='records')
for i in range(0,len(dict_p)):
    frist = True
    values = ''
    for i_col in list_columns:
        if(frist):
            if(type(dict_p[i][i_col]) is float or type(dict_p[i][i_col]) is int ):
              values = "'" + str(int(dict_p[i][i_col])) + "'" 
              frist = False
            else:
                values = "'" + str(dict_p[i][i_col]) + "'" 
                frist = False
        else:
            if(type(dict_p[i][i_col]) is float or type(dict_p[i][i_col]) is int ):
                values = values + ',' + "'" + str(int(dict_p[i][i_col])) + "'" 
            else:
                values = values + ',' + "'" + str(dict_p[i][i_col]) + "'" 
    queryfinal = columnQuery + values + ")"
    # Need to create a func for validate 
    ArrayFinalInsert.append(queryfinal)


notepad = r"C:\Windows\System32\notepad.exe"   # Path to Notepad application
filename = "example.txt"                      # Name of the file to be created

open('example.txt', 'w').close() #clean data in file
import subprocess
import pyautogui
import time

file1 = open("example.txt","w")



#Headres dor Validate if table have data;
headres = ['DECLARE @rowCount int = (select count(*) from ' + TableName +')', 'select @rowCount;','IF (@rowCount = 0)','BEGIN'] 
for s in headres:
    file1.write(s + "\n")

for s in ArrayFinalInsert:
    file1.write("\t" + s + "\n")
#END INSERTS;
file1.write('END')
file1.close() #to change file access modes

