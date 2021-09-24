import wget

print('Beginning file download with wget module')

url = 'https://github.com/WentworthJin/Unit_Budget_Planner/raw/master/Unit_Budget/Unit%20testing%20file/CITS4401_Sem1%202021%20budgetv3.xlsx'
wget.download(url, '../Downloads/CITS4401_Sem1 2021 budgetv3')