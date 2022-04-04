#!/usr/bin/env python3
from common_variables import years, Current_year

import pandas as pd
from datetime import date, timedelta

import current_year
import previous_years

#Checking if the year is current or previous and calling the respective functions

for year in years:
 if int(year)==Current_year:
  current_year.current_year()
 else:
  previous_years.previous_years(year)