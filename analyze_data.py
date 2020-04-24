#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 10:00:34 2020

@author: ware.cole
"""

# 1 - import
import pandas as pd

# 2 - read csv
mapped = pd.read_csv("gis_output.csv")

# 3 - replace NaN values for blocks not inside rings
mapped["ringId"].fillna(3, inplace = True)

# 4 - set labels for rings
within5 = mapped["ringId"] == 1
within10 = mapped["ringId"] == 2
outside = mapped["ringId"] == 3

mapped.loc[within5, "ring"] = "<5 mi"
mapped.loc[within10, "ring"] = ">5, <10 mi"
mapped.loc[outside, "ring"] = ">10 mi"

# 4 - group by ring
by_ring = mapped.groupby("ring")

# 5 - sum vets in each cohort by ring
print("Vets, 18-34:")
sum_18to34 = sum(mapped["vet_data_18to34_total"])
rings_18to34 = by_ring["vet_data_18to34_total"].sum()
print(round(rings_18to34/sum_18to34, 3))

print("Vets, 35-54:")
sum_35to54 = sum(mapped["vet_data_35to54_total"])
rings_35to54 = by_ring["vet_data_35to54_total"].sum()
print(round(rings_35to54/sum_35to54, 3))

print("Vets, 55-64:")
sum_55to64 = sum(mapped["vet_data_55to64_total"])
rings_55to64 = by_ring["vet_data_55to64_total"].sum()
print(round(rings_55to64/sum_55to64, 3))

print("Vets, 65-74:")
sum_65to74 = sum(mapped["vet_data_65to74_total"])
rings_65to74 = by_ring["vet_data_65to74_total"].sum()
print(round(rings_65to74/sum_65to74, 3))

print("Vets, 75+:")
sum_75up = sum(mapped["vet_data_75up_total"])
rings_75up = by_ring["vet_data_75up_total"].sum()
print(round(rings_75up/sum_75up, 3))