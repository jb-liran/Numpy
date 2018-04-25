# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 18:20:54 2015

@author: liran
"""

from scipy.interpolate import interp1d
from pylab import plot, axis, legend
from numpy import *

# sample values
x = linspace(0,2*pi,6)
y = sin(x)


spline_fit = interp1d(x,y,kind=5)
xx = linspace(0,2*pi, 50)
yy = spline_fit(xx)

# display the results.
plot(xx, sin(xx), 'r-', x,y,'ro',xx,yy, 'b--',linewidth=2)
axis('tight')
legend(['actual sin', 'original samples', 'interpolated curve'])







