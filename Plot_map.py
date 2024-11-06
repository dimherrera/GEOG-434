#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:04:31 2024

@author: dimitrisherrera
"""

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

# Load the data
pr = xr.open_dataset('/Users/dimitrisherrera/Downloads/precip.mon.ltm.0.25x0.25.v2020.nc')
pre = pr.precip

# Calculte the annual mean
mean = pre.groupby('time.year').mean(dim='time')

# Plot the data
fig, ax = plt.subplots(figsize=(7,5))
yi = plt.imshow(mean[0,:,:], vmin=0, vmax=200, cmap='rainbow')
plt.title('Global mean precipitation',fontsize=15)
cbar = plt.colorbar(yi, orientation='horizontal', fraction=0.08,anchor=(1.0,1), pad=0.05)
cbar.set_label('mm', fontsize=12, labelpad=3)
ax.axes.get_xaxis().set_ticks([])
ax.axes.get_yaxis().set_ticks([])
plt.tight_layout()