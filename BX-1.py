# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 12:19:28 2021

@author: Mr Minion
"""

import numpy as np #Numerical inputs, functions, and conditions
x1 = 1.4 #x-coordinate of m1 body // #[AU]
x2 = 2.5 #x-coordinate of m2 body // #[AU]

y1 = 0 #y-coordinate of m1 body // #[AU]
y2 = 0 #y-coordinate of m2 body // #[AU]

m1 = 1e9 #An obiting body with mass m1 // #[Kg] 
m2 = 2e9 #An obiting body with mass m2 // #[Kg]
M = 1e18 #A massive body at center // #[Kg]

r1 = 1.4 #Radius of m1 body from the center // #[AU]
r2 = 2.5 #Radius of m2 body from the center // [AU]

G = 1.98284656*1e-29 #Gravitional constant // [Kg^-1*AU^3*yr^-2]
w1 = np.sqrt(G*M/r1**3) #Angular velocity of m1 body // [radian*yr^-1]
w2 = np.sqrt(G*M/r2**3) #Angular velocity of m2 body // [radian*yr^-1]

t = np.linspace(0, 1, num = 365) #Time period [1 observation/day] for upto a Year // [yr]
wrt1 = w1*r1*t #product of w, r, and t // [AU]
wrt2 = w2*r2*t 

for i in range(len(t)): #Looping x1, x2, y1, and y2
    x1 = x1 + wrt1
    y1 = y1 + wrt1
    x2 = x2 + wrt2
    y2 = y2 + wrt2

r1new = np.sqrt((x1)**2 + (y1)**2) 
r2new = np.sqrt((x2)**2 + (y2)**2)
p1 = r1new - r2new #Variation in the position of m1 body with reference to m2 body // [AU]
p2 = r2new - r1new #Variation in the position of m2 body with reference to m1 body // [AU]

for i in range(len(t)): #Looping t to verify of observations done
    if t[i]:
        print(i) #array starts with '0' so please include it  
        
import matplotlib.pylab as plt #Plotting
plt.subplot(2, 1, 1) 
plt.plot(t, p1, 'b--')
plt.xlabel("Time [yr]", fontsize = 7)
plt.ylabel("Position variation [AU]", fontsize = 7)
plt.legend(['m1 observed by m2'])
plt.grid()
plt.subplot(2, 1, 2)
plt.plot(t, p2, 'r--')
plt.xlabel("Time [yr]", fontsize = 7)
plt.ylabel("Position variation [AU]", fontsize = 7)
plt.legend(['m2 observed by m1'])
plt.grid()
        



    