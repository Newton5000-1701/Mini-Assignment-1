#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:59:54 2024

@author: isaacthompson
"""

import numpy as np
import matplotlib.pyplot as plt


A = 10  # V/m
a = 2   # meters
k = 0.4  # 1/m

x = np.arange(0, 20.1, 0.1)

E = A * np.cos(np.pi * x / a) * np.exp(-k * x)

# Plot the result
plt.figure(figsize=(8, 6))
plt.plot(x, E, label='E(x) = A*cos(pi*x/a) * e^(-kx)', color='b')
plt.title('Electric Field along the Waveguide')
plt.xlabel('Position (m)')
plt.ylabel('Electric Field (V/m)')
plt.grid(True)
plt.legend()
plt.show()

