#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 07:58:21 2017

@author: liran
"""
import scipy as sc
import scipy.stats as scs
import pylab as py

x= scs.norm.pdf(sc.r_[-5:5:100j])
py.plot(x)
py.show()