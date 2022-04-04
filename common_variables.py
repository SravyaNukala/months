#!/usr/bin/env python3
import pandas as pd
from datetime import date, timedelta

#Keeping frequently used variables. In future, team can change the variable values in this file alone
#Enter S3 bucket name in the bucket_name variable

years= ['2020', '2021', '2022']
todays_date = date.today()
Current_year = todays_date.year
months_num = ["01","02","03","04","05","06","07","08","09","10","11","12"]
days_num = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
bucket_name=<bucket_name>