#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Panagiotis
# @Date:   2015-07-27 11:54:23
# @Last Modified by:   Panagiotis
# @Last Modified time: 2015-07-30 18:18:33

import etg2hdmap

def etg2hd(df, column, etg2hd_map):
	tempDf = df #.copy() TODO see if you are going to copy
	all_etg_key_lists = etg2hd_map.values()
	all_etg_keys = [etg_key for etg_key_list in all_etg_key_lists for etg_key in etg_key_list]
	
	etg_values = df[column].unique()
	new_etg_values = list(set(etg_values) - set(all_etg_keys))
	if len(new_etg_values)>0:
		raise ValueError('There are unexpected etg values: Column: %s, Values: %s' % (column, new_etg_values))

	for hd_key, etg_keys in etg2hd_map.items():
		for etg_key in etg_keys:
			tempDf[column] = df[column].replace(etg_key, hd_key)	
	return tempDf

def mapping(idf):
	"Gets Vehicles raw data and replaces Greek with English while grouping some in HD categories"
	df = idf.copy()
	df['NumberOfDoors'] = df['NumberOfDoors'].astype(str) 
	var_names = [var for var in dir(etg2hdmap) if not (var.startswith('__') and var.endswith('__'))]
	for var_name in var_names:
		var_map = getattr(etg2hdmap, var_name)
		df = etg2hd(df, var_name, var_map)
	return df

# df_ExcludedBodyTypeVehicles = df_vehicles[~df_vehicles['BodyType'].isin(['4x4','Cabriolet','Coupé','Estate','Hatchback','MPV','Saloon'])]
def afunction(df):
	exludeReasons = ['BodyType', 'EUEmissionsTierConformance', 'Manufacturer', 'Segmentation']
	for reason in exludeReasons:
		
	return