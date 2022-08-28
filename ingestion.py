###import packages
import pandas as pd 
import xlrd 
import requests
import json

#####SECTION1

##import local xls file 
df = pd.read_excel('/Users/laynejohnson/Documents/GitHub/hha-data-ingestion/Data/covid19tracker.xls')


xls = xlrd.open_workbook('/Users/laynejohnson/Documents/GitHub/hha-data-ingestion/Data/covid19tracker.xls', on_demand=True)
xls.sheet_names()


###tabs named
tab1 = pd.read_excel('/Users/laynejohnson/Documents/GitHub/hha-data-ingestion/Data/covid19tracker.xls', sheet_name= 'Health Policy Response')
tab2 = pd.read_excel('/Users/laynejohnson/Documents/GitHub/hha-data-ingestion/Data/covid19tracker.xls', sheet_name= 'Country coverage')
tab3 = pd.read_excel('/Users/laynejohnson/Documents/GitHub/hha-data-ingestion/Data/covid19tracker.xls', sheet_name= 'Other Policy Tracking Sites')



####SECTION2

###Using requests package to call in CMS dataset
apiDataset = requests.get('https://data.cms.gov/data-api/v1/dataset/c8a139ee-9e31-444c-976f-bab6b287b871/data')
apiDataset = apiDataset.json()



###SECTION3