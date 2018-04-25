# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 18:20:54 2015

@author: liran
"""

from scipy.interpolate import interp1d
from pylab import plot, axis, legend
import numpy as np


xdata = np.array([-2,-1.64,-1.33,-0.7,0,0.45,1.2,1.64,2.32,2.9])
ydata = np.array([0.699369,0.700462,0.695354,1.03905,1.97389,2.41143,1.91091,0.919576,-0.730975,-1.42001])

spline_fit = interp1d(xdata,ydata,kind=5)
xx = np.linspace(np.min(xdata),np.max(xdata), 50)
yy = spline_fit(xx)

# display the results.
plot(xdata,ydata,'ro',xx,yy, 'b--',linewidth=2)
axis('tight')
legend([ 'original samples', 'interpolated curve'])







