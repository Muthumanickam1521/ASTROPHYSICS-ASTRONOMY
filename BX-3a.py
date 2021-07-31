# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 13:15:08 2021

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

# (a.) Extracting the binary system parameters
def paractor():
    
   for i in range(len(L0)):
        if L0[i] > 0:
            print('''Brightness is one of the parameters''')
            return True
        
       
if paractor() is True:
    print('''Luminousity is one of the parameters''')
    if paractor() is False:
        print('''No revolving''')
    elif paractor() is True:
        print('''Revolving is one of the parameters''')
            

def period():
    for i in range(len(P)):
         if P[i] > 0:
           return True
    
if period() is True:
     print('''Obiting period is one of the parameters''')  
if period() is False:
     print('''Orbiting period is not one of the parameters''')
        
  
                    
                                  
                                    
              
              
              
        
        