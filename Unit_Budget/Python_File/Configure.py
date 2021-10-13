import pandas as pd
# This is the file for keep all the constant variables.








'''
   *** the following code is for retrive data from excel to dataframe
   *** this specify the range of each block/table
   *** if you want to modify the excel file template, you need to modify following get_details function accordingly.

'''

def get_details(file):
  unit_detail = pd.read_excel(file,usecols ="A:F",header =5,nrows=7)
  teaching_team = pd.read_excel(file,usecols ="A:Z",header =15,nrows=4)
  delivery = pd.read_excel(file,usecols ="A:Z",header =24,nrows=16)
  marking = pd.read_excel(file,usecols ="A:Z",header =43,nrows=6)
  NSC = pd.read_excel(file,usecols ="A:Z",header =53,nrows=7)
  return unit_detail,teaching_team,delivery,marking,NSC


