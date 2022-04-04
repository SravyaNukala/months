#!/usr/bin/env python3
from common_variables import months_num, days_num

import pandas as pd
from datetime import date, timedelta
import delete_folders

#Will send the dates of previous years to delete_folders script. Every month first date folders won't get deleted

def previous_years(year):
  for i in months_num:
    for j in range(30):
       previous_year_days=str(days_num[j+1])+"-"+str(i)+"-"+str(year)
       delete_folders.delete_folder(year,i,previous_year_days)