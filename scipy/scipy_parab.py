#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 21:16:36 2017

@author: liran
"""

import scipy as sc
import numpy as np
import pylab as py

def fx(x):
    return 2*(x[0]**2) + 10

def fx1(x):
    return 2*(x**2) + 10

x=np.linspace(-20,20,100)

y1=fx1(x)
py.plot(x,y1)

fopt= sc.optimize.fmin(fx,x, full_output=True, disp=False)
print (fopt[1])
