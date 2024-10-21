#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:05:05 2024

@author: isaacthompson
"""

import matplotlib.pyplot as plt
from datetime import datetime

file_name = 'fismflux20020824.dat'


times = []
bin_56 = []


with open(file_name, 'r') as file:
    next(file) #skip header
    
    for line in file:
        data = line.split()
        
        date_str = ' '.join(data[:6])
        
        bin_56_value = float(data[61])
        
        times.append(datetime.strptime(date_str, '%Y %m %d %H %M %S'))
        bin_56.append(bin_56_value)

plt.figure(figsize=(10, 6))
plt.plot(times, bin_56, label='56th bin of EUV spectrum', color='b')
plt.title('56th Bin of EUV Spectrum as a Function of Time')
plt.xlabel('Time')
plt.ylabel('Irradiance (W/m²/nm)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()
