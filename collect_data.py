#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 10:44:53 2020

@author: ware.cole
"""

# 1 - imports
import pandas as pd
import requests

# 2 - read csv file to set var_info to desired variables
var_info = pd.read_csv("veteran_variables.csv")

# 3 - convert the Pandas series into a list
var_name = var_info["variable"].to_list()

# 4 -  include name of geographic entity with each row

var_list = ["NAME"]+var_name

# 5 - concatenate the list into a comma separated string
var_string = ",".join(var_list)

# 6 - set api to ACS 2018
api = 'https://api.census.gov/data/2018/acs/acs5'

# 7 - set FIPS code for all block groups within a county
for_clause = "block group:*"

# 8 - for loop retrieving data on each county 

counties = ["005", "007", "019", "029", "035", "043", "055", "067", "075", 
            "077", "081", "085", "093", "099", "103", "133", "139", "151", 
            "153", "155","157", "169"]

master = pd.DataFrame()

for county in counties:
    in_clause = "county:"+county+" state:39"
    payload = {"get":var_string, "for":for_clause, "in":in_clause}
    response = requests.get(api, payload)
    row_list = response.json()
    colnames = row_list[0]
    datarows = row_list[1:]
    data = pd.DataFrame(columns = colnames, data = datarows)
    data.set_index('NAME', inplace = True)
    master = master.append(data)

# 9 - create geoids
    
master["geoid"] = master["state"] + master["county"] + master["tract"] + master["block group"]

# 10 - write to csv
master.to_csv("veteran_data.csv")