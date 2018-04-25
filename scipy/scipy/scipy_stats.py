#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 08:44:11 2018

@author: liran
"""

import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

s=np.r_

rv1 = stats.norm()
rv2 = stats.norm(2.0,0.8)
samp = s[rv1.rvs(size=100), 
	           rv2.rvs(size=100)]
# Kernel estimate (smoothed histogram)
apdf = stats.kde.gaussian_kde(samp)
x = np.linspace(-3,6,200)
plt.plot(x, apdf(x),'r')

# Histogram
#plt.hist(x*10, bins=250, normed=True)
