# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 18:46:56 2021

@author: Mr Minion
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

#Test function given by BOSE.X Team
L0 = np.array([6333.938,6243.194,6170.599,6152.45,6152.45,6152.45,6188.748,6243.194,6243.194,6098.004,6152.45,6098.004,6098.004,6079.855,5989.111,5898.367,5735.027,5553.539,5335.753,5117.967,4718.693,4065.336,3411.978,2958.258,2286.751,1996.37,1851.18,1887.477,1887.477,1996.37,2304.9,2758.621,3230.49,3811.252,4029.038,4228.675,4373.866,4573.503,4682.396,4863.884,4990.926,5499.093,5662.432,5880.218,6061.706,6188.748,5989.111,5970.962,6061.706,5952.813,6025.408,6043.557,6043.557,6007.26,5989.111,5589.837,5408.348,5390.2,5680.581,5517.241,5843.92,5952.813,5989.111,5989.111,5916.515,5916.515,5989.111])
P = np.linspace(0,1,len(L0))
f = interpolate.interp1d(P,L0*1e5)
xnew = np.linspace(0, 1, 1000)
ynew = f(xnew) 
plt.plot(xnew,ynew+np.random.random(1000)*1e8)
plt.yscale('log')
plt.ylabel('Intensity',fontsize=21)
plt.xlabel('Period',fontsize=21)
plt.grid()

# (c.)Predicting the fate of the stars

## CCSNe prediction
Threshold1_L0 = 1e9*3.1104*1e7 ### Threshold luminousity for the CCSNe to occur
                               ### It's been calculated with respective to the luminousity chart for my convenient                 
for i in range(len(L0)):
     if L0[i] >= Threshold1_L0:
         print(i, '''CCSNe does occur''')
     elif L0[i] <= Threshold1_L0:
         print('''CCSNe doesn't occur''')
        
## SNe prediction
def SN_P():
    Threshold2_L0 = 1.5*1e7*25.4*3.1104*1e7 ###Threshold luminousity for the SNe to occur
                                            ###It's been calculated with Sirius star as a reference for the Super Nova formation and theorisied separately                       
    for i in range(len(L0)):
        if L0[i] >= Threshold2_L0:
            print(i, '''SNe formation does take place''')
            return True
        elif L0[i] <= Threshold2_L0:
            print('''SNe formation doesn't take place''')
            return False
            
## Neutron star prediction
if SN_P() is True: ### If SNe has formed
    print('''Neutron star formation does happen''')
elif  SN_P() is False: ### If SNe hasn't formed yet
    print('''Neutron star formation doesn't happen''') 
          
## Blackhole prediction
if SN_P() is True: ### If SNe has formed
    print('''Blackhole formation does happen''')
elif  SN_P() is False: ### If SNe hasn't formed yet
    print('''Blackhole formation doesn't happen''') 

          
          
                                        
                           
                                        
                                    
                                    
              
              
              
        
        