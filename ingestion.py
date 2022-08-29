###import packages
import pandas as pd 
import xlrd 
import requests
import json
from google.cloud import bigquery

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

##Creating client variable to connect to authentication key
client = bigquery.Client.from_service_account_json('/Users/laynejohnson/Desktop/data-ingestion-360914-3248b6fda89f.json')

##Creating query_job to access province table of dataset
query_job = client.query("SELECT * FROM `bigquery-public-data.covid19_italy.data_by_province` LIMIT 100")

##Results
results = query_job.result() 
###receiving error- bigquery-public-data was not found in location US

##Results into dataframe
bigquery1 = pd.DataFrame(results.to_dataframe()) 
###recieving error - no module named 'db_dtypes' - did pip install command - now recieving 'results' is not defined


###creating query_job to access region table of dataset
query_job_2 = client.query("SELECT * FROM `bigquery-public-data.covid19_italy.data_by_region` LIMIT 100")

##results 
results_2 = query_job_2.result()

###results into dataframe
bigquery2 = pd.DataFrame(results_2.to_dataframe())