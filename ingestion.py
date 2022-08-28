###import packages
import pandas as pd 
import xlrd ## import xlrd for excel files, tab names 

##import local xls file 
df = pd.read_excel('/Users/laynejohnson/Documents/GitHub/hha-data-ingestion/Data/covid19tracker.xls')


xls = xlrd.open_workbook('/Users/laynejohnson/Documents/GitHub/hha-data-ingestion/Data/covid19tracker.xls', on_demand=True)
xls.sheet_names()

###xls to dataframe
df = pd.read_excel('/Users/laynejohnson/Documents/GitHub/hha-data-ingestion/Data/covid19tracker.xls', sheet_name= 'Health Policy Response')
df = pd.read_excel('/Users/laynejohnson/Documents/GitHub/hha-data-ingestion/Data/covid19tracker.xls', sheet_name= 'Country coverage')
df = pd.read_excel('/Users/laynejohnson/Documents/GitHub/hha-data-ingestion/Data/covid19tracker.xls', sheet_name= 'Other Policy Tracking Sites')


###tabs named
tab1 = pd.read_excel('/Users/laynejohnson/Documents/GitHub/hha-data-ingestion/Data/covid19tracker.xls', sheet_name= 'Health Policy Response')
tab2 = pd.read_excel('/Users/laynejohnson/Documents/GitHub/hha-data-ingestion/Data/covid19tracker.xls', sheet_name= 'Country coverage')
tab3 = pd.read_excel('/Users/laynejohnson/Documents/GitHub/hha-data-ingestion/Data/covid19tracker.xls', sheet_name= 'Other Policy Tracking Sites')