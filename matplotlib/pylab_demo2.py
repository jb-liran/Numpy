# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 17:54:04 2015

@author: liran
"""
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    s1 = np.cos(2*np.pi*t)
    e1 = np.exp(-t)
    return np.multiply(s1,e1)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
t3 = np.arange(0.0, 2.0, 0.01)

plt.subplot(2,2,1)
l = plt.plot(t1, f(t1), 'bo', t2, f(t2),'k--')
plt.setp(l, 'markerfacecolor', 'g')
plt.grid(True)
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')

plt.subplot(2,2,2)
plt.plot(t3, np.cos(2*np.pi*t3), 'r.')
plt.grid(True)
plt.xlabel('time (s)')
plt.ylabel('Undamped')


plt.subplot(223)
l = plt.plot(t1, f(t1), 'bo', t2, f(t2),'k--')
plt.setp(l, 'markerfacecolor', 'g')
plt.grid(True)
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')

plt.subplot(224)
plt.plot(t3, np.cos(2*np.pi*t3), 'r.')
plt.grid(True)
plt.xlabel('time (s)')
plt.ylabel('Undamped')
plt.show()
