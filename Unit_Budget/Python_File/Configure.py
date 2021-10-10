# This is the file for keep all the constant variables.



# the max number of teaching staff and Non Salary Cost item
max_teacher=10
max_NSC = 6





'''
   *** the following code is for retrive data from excel to dataframe
   *** this specify the range of each block/table
   *** if you want to modify the excel file template, you need to modify following get_details function accordingly.

'''

def get_details(file):
  unit_detail = pd.read_excel(file,usecols ="A:L",header =8,nrows=5)
  unit_strcture = pd.read_excel(file,usecols ="A:J",header =29,nrows=13)
  resourcing = pd.read_excel(file,usecols ="A:L",header =46,nrows=9)
  NSC = pd.read_excel(file,usecols ="A:F",header =62,nrows=4)
  return unit_detail,unit_strcture,resourcing,NSC


