#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Panagiotis
# @Date:   2015-07-27 11:54:23
# @Last Modified by:   Panagiotis
# @Last Modified time: 2015-07-30 18:18:33

import pandas as pd
import numpy as np
import etg2hdmap

def etg2hd(df, column, etg2hd_map):

	all_etg_key_lists = etg2hd_map.values()

	all_etg_keys = [etg_key
		for etg_key_list in all_etg_key_lists
			for etg_key in etg_key_list]

	etg_values = df[column].unique()

	new_etg_values = list(set(etg_values) - set(all_etg_keys))
	if len(new_etg_values)>0:
		raise ValueError('There are unexpected etg values: Column: %s, Values: %s' % (column, new_etg_values))


	for hd_key, etg_keys in etg2hd_map.iteritems():
		for etg_key in etg_keys:
			df[column] = df[column].str.replace(etg_key, hd_key)	
	return df

def mapping(df):
	"Gets Vehicles raw data and replaces Greek with English while grouping some in HD categories"
	
	df = etg2hd(df, 'TransmissionType', etg2hdmap.TransmissionType)
	df = etg2hd(df, 'BodyType', etg2hdmap.BodyType)
	df = etg2hd(df, 'BreaksType', etg2hdmap.BreaksType)
	return df
