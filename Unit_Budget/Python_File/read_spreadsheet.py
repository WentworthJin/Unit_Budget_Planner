import openpyxl
import json

file = "CITS1001_Sem1,2021 budget v3.xlsx"
#file path

def resourcing_data(file):
    spreadsheet = openpyxl.load_workbook(file)
    sheet = spreadsheet['Unit budget']
#open spreadsheet and load the unit budget sheet
    for i in range(40,60):
        if sheet['A'+str(i)].value == 'Name':
            start_row = i + 1
#find first row
    end_row = -1
    row = start_row
    while end_row == -1:
        if sheet['A'+str(row)].value == 'Total':
            end_row = row
        else:
           row = row + 1
#find last row
    j = 0
    datalist = []
    for i in range(start_row,end_row-1):
       name = sheet['A'+str(i)].value
       if name != None:
            resourcing = [{'Name':name,'Type':sheet['B'+str(i)].value,'TeachingCode':sheet['C'+str(i)].value,'Lectures':sheet['D'+str(i)].value,'Workshops':sheet['E'+str(i)].value,'Laboratories':sheet['F'+str(i)].value}]   #,'MCI':sheet['G'+str(i)].value,'Marking':sheet['H'+str(i)].value,'Training':sheet['I'+str(i)].value,'TotalHours':sheet['J'+str(i)].value,'Cost':sheet['K'+str(i)].value
            datalist.append(json.dumps(resourcing))
            j = j + 1   
    
    return(datalist)

list = resourcing_data(file)
for i in range(0,len(list)):
    print(list[i])


