#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 11:48:57 2020

@author: ware.cole
"""

# 1 - import
import pandas as pd

# 2 - read the data file and set the index
data = pd.read_csv("veteran_data.csv", index_col= "NAME")

# 3 - combine columns across sex for each age cohort
data["18to34_total"] = data["B21001_008E"] + data["B21001_026E"]
data["35to54_total"] = data["B21001_011E"] + data["B21001_029E"]
data["55to64_total"] = data["B21001_014E"] + data["B21001_032E"]
data["65to74_total"] = data["B21001_017E"] + data["B21001_035E"]
data["75up_total"] = data["B21001_020E"] + data["B21001_038E"]

# 5 - write to csv
data.to_csv("clean_veteran_data.csv")