#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# convivaConverter.py v2 - Re-formats BAMTECH Conviva Data for Amazon quicksight
# Written by Ross Kanter 2018


import csv, os, glob, re, shutil, sys
import numpy as np
import pandas as pd



os.chdir('./ConvivaData/')

# Loop through every file in the current working directory.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue # skip non-csv files

    print('Slicing ' + csvFilename + '...')
    # Read the CSV file in (skipping first row).
    csvRows = []
    with open(csvFilename) as csvFileObj:
        readerObj = csv.reader(csvFileObj)
        for row in readerObj:
            if readerObj.line_num <= 11 or len(row) < 2:
                continue # skip first 12 rows
            csvRows.append(row)
            
                
        # csvFileObj.close()


        # Write out the CSV file in 3 sections without blank rows in new directory
        # csvFileObj = open(os.path.join('ProcessedConvivaData', ('slice 1 ' + csvFilename)), 'w', newline='')
        # csvWriter = csv.writer(csvFileObj)
        table_1 = []
        for row in csvRows[:289]:
            if row:
                table_1.append(row)

        table_2 = []
        for row in csvRows[289:578]:
            if row:
                table_2.append(row)

        table_3 = []
        for row in csvRows[578:]:
            if row:
                table_3.append(row)

    df_1 = pd.DataFrame(table_1)
    df_2 = pd.DataFrame(table_2).drop(0, axis=1)
    df_3 = pd.DataFrame(table_3).drop(0, axis=1)
    print('Merging Files into QuicksightReady file')
#os.chdir('./ProcessedConvivaData')

#loop through slices and concatenate into one CSV by column using pandas

# list_of_slices = []

#for root, dirs, files in os.walk('.', topdown = True):
    #if x <= 3:
         
         #for file in files:
         #list_of_slices.append(os.path.join(root, file))
            #x = x + 1
    
    combined_csv = pd.concat([df_1, df_2, df_3], ignore_index = True, axis = 1)
    combined_csv = combined_csv.replace('\w\w\w\s\d\d\s\d\d\d\d', '', regex=True)
    combined_csv.to_csv("./QuicksightReady.csv", index=False, header=False)
    os.rename("./QuicksightReady.csv", "Quicksight_" + csvFilename)

# delete the 3 slices so that only the original and final CSVs remain in the directory
# consider looping throug multiple conviva csv's at once and tackle problem of combining the correct slices with control flow

    
   
