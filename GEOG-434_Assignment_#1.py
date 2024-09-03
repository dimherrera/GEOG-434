#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 13:25:06 2024

@author: dimitrisherrera
"""

import xarray as xr
import pandas as pd
import numpy as np

# Load the CSV data
data = pd.read_csv('/Users/dimitrisherrera/Downloads/Knoxville_pre.csv')
data = data.set_index('time')
data.index = pd.to_datetime(data.index)

# Calculate the climatology/long-term means
clim = data.groupby(data.index.month).mean()

# Calculate the anomaly
anom = data['prcp'] - data.groupby(data.index.month)['prcp'].transform('mean')  

# Calculate standard deviations
std_data = data.std()
std_anom = anom.std()

# Calculate trend
trend = np.ma.polyfit(np.arange(0,852,1), data['prcp'].values, 1)[-2]
