#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 07:52:06 2018

@author: liran
"""

import scipy.signal as ssig
import matplotlib.pyplot as plt
import skimage.data as skd

img = plt.imread('/Users/liran/python.png')

#plt.imshow(img)

img = ssig.medfilt(img)

plt.imshow(img)
