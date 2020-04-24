#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 11:48:37 2020

@author: ware.cole
"""

SPATIAL ANALYSIS OF VA CLINICS IN NORTHEAST OHIO RELATIVE TO VETERANS BY AGE COHORT

1: Purpose

To make medical care accessible, the VA locates its clinics near the veterans
it serves. Like any demographic, veterans move in and out of areas over
time. Yet these residential changes are slow, so it is rare for the VA to have
to close or move a clinic. 

Currently, however, the VA is undergoing a shift in the population it serves. 
Increasingly, the VA provides care to younger veterans. Since housing is 
somewhat segregated by age, it is conceivable that the VA's clinics will 
not be efficiently located to serve this younger population. 

This analysis aims to determine whether the VA clinics in Northeast Ohio
are equally accessible to veterans across age cohorts.

2: Sources of Data

To perform this analysis, the following data were required. The source of 
each is noted.

    > Data on the veteran population by block group, specifically age 
    breakdowns. This information is available from the Census, in the 2018 
    American Community Survey. (The "collect_data.py" script will
    retrieve this data.)
    > The shapefile for the block groups in question. This information is
    available from TIGER/Line Shapefiles page on the Census website.
    > Locations of the VA clinics. This data was retrieved manually from the 
    VA website, and the addresses were inputted into QGIS.
    
3: Process of Analysis

    1) Run the "collect_data.py" script. This script takes the relevant 
    variables, listed in the "veteran_variables.csv" file, constructs an 
    API call, and retrieves the data from the Census. The result is CSV file
    containing the relevant data on veterans for the requested block groups.
    2) Run the "clean_data.py" script. This script prepares the data for
    analysis in QGIS. Specifically, it creates and labels variables for the
    total population of veterans in given block groups broken down by age
    cohort. 
    3) Conduct an analysis on QGIS. Broadly, this involves the following:
        a) Load the shapefile including the block groups for Ohio.
        b) Filter out the counties not included in the analysis for 
        Northeast Ohio.
        c) Use the centroids processing algorithm to place centroids for each
        block group.
        d) Overlay the clinic locations. By importing a CSV file with the 
        addresses, the locations can be added. Dissolve this layer.
        e) Using the multi-ring buffer function, add two rings around the 
        clinic locations. The distance interval should be 5 miles.
        f) Onto the block group centroids, join the buffer.
        g) Export the joined layer to a CSV file, including the variables 
        about veteran population by age cohort and the "ringId" variable.
    4) Run the "analyze_data.py" script. This script marks each block group
    by whether it is within 5 miles, 10 miles, or beyond 10 miles from a 
    clinic. From this, it calculates the proportion of veterans living within
    those "rings" broken down by age cohort.