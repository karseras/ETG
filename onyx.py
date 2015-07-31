#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Panagiotis
# @Date:   2015-07-27 11:55:00
# @Last Modified by:   Panagiotis
# @Last Modified time: 2015-07-30 18:13:46

import pandas as pd
import numpy as np
import re
import auxilary

# def isValidFunc(df_in):
#    "Takes and returns DataFrame"
#    df_out = df_in.loc[df_in['ETGCode'].notnull() & df_in['ETGCode'].apply(np.isreal) & (df_in['ETGCode']>0) & (df_in['ETGCode']<10000000) & df_in['Manufacturer'].notnull() & df_in['Manufacturer'] & (df_in['Manufacturer'].apply(len)>1) & (df_in['Manufacturer'].apply(len)<21) & df_in['Model'].notnull() & isinstance(df_in['Model'], str) & (df_in['Model'].apply(len)>0) & (df_in['Model'].apply(len)<51)]
#    return df_out

### Import raw data from csv
df_old = pd.read_csv("C:\ETG\OLD.csv")    # old result of the ETG software for comparison
df_vehicles = pd.read_csv("C:\ETG\TOTAL - copy.csv")
df_price = pd.read_csv("C:\ETG\PRICE.csv")

df_vehicles.columns = ['ETGCode','veh_type','Manufacturer','Model','ModelLine','Type','BodyType','AvailableFrom','AvailableTo','EngineCapacityCC','PowerKW','PowerHP','TaxablePowerHP','TransmissionType','NumberOfGears','NumberOfDoors','NumberOfSeats','WheelDrive','FuelInjection','Acceleration_0-100Km','FuelType','MaximumSpeed_Km_Per_h','NetWeightKg','EUEmissionsTierConformance','CO2Emissions_g_Per_Km','Segmentation','BreaksType','metallicRoof','fabricRoof']
df_price.columns = ['ETGCode','YearOfRegistration','CurrentRetailPrice','CurrentWholeSalePrice']

df_vehicles = df_vehicles.set_index('ETGCode')
df_price = df_price.set_index('ETGCode')

### 1: Check for invalid values

### 2: normalize raw input data
df_normalizedVehicles = auxilary.mapping(df_vehicles) # According to etg2hdmap file


#df_vehicles = df_vehicles[df_vehicles['BodyType'].isin(['4x4','Cabriolet','Coupé','Estate','Hatchback','MPV','Saloon'])]

### 3: Grouping?


#regex = pd.read_csv("C:\ETG\patterns1.csv")
#df_vehicles['Model'] = df_vehicles['Model'].replace(myDict.model, regex=True)

### OUTPUT
#df_vehicles.to_csv('C:\ETG\output_vehicles.csv', mode='w', encoding='utf8')
#df_price.to_csv('C:\ETG\output_price.csv', mode='w', encoding='utf8')
