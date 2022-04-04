#!/usr/bin/env python3
from common_variables import years, Current_year, months_num

import pandas as pd
from datetime import date, timedelta
import delete_folders

all_dates=[]
exception_dates=[]
retaining_dates=[]

#Will send the dates of current year to delete_folders script. Every Monday date folders and past seven days folders won't get deleted.

def allmondays(year):
    return pd.date_range(start=str(year), end=str(year+1),
                         freq='W-MON').strftime('%d-%m-%Y').tolist()

def exception_days():
    for i in range(7):
        past_seven_days=((date.today()-timedelta(days=(i))).strftime("%d-%m-%Y"))
        exception_dates.append(str(past_seven_days))

    for a in allmondays(Current_year):
        exception_dates.append(a)

    return exception_dates
    
def all_days():
    start_date = date(Current_year, 1, 1)
    end_date = date.today()
    delta = end_date - start_date

    for i in range(delta.days + 1):
        day = (start_date + timedelta(days=i)).strftime("%d-%m-%Y")
        all_dates.append(day)
    return all_dates

def current_year():
  retaining_dates=exception_days()
  total_days=all_days()
  final_days = [i for i in total_days if i not in retaining_dates]
  for month in months_num:
      for x in final_days:
          delete_folders.delete_folder(Current_year,month,x)    