# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:29:25 2020

@author: magnehi
"""

import numpy as np
N=np.array([-1,   0,   0,  0,      # C1
             0,  -1,   0,  0,      # C2
             0,   0., -1,  0,      # C3
             0,   0,   0, -1,      # C4
             1,   2,   3,  4,      # CO2
             2,   3,   4,  5,      # H2O
            -2, -3.5, -5, -6.5,    # O2
             0,   0,   0,  0])     # N2
print(N)
N.shape=(8,4)
print(N)

X=np.array([1, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 0, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 0, 0, 0])
X.shape=(4,8)

R=( np.eye(8) + np.dot(N,X) )
print(R)
#               C1   C2   C3  C4  CO2  H2O  O2  N2
FFuel=np.array([80., 10., 5., 5., 0.,  0.,  0., 0.,])
FAir =np.array([ 0.,  0., 0., 0., 0.,  0., 21., 79.,])*12.0238   # stoichiometric = (80*2+10*3.5+5*5+5*6.5)/21
FAir = FAir*1.20    

F0=FFuel + FAir

F1=R@F0  # same as F1=np.dot(R,F0)

print('F1=',F1)

print('F1 tot=',F1.sum())

print('y1=',F1/F1.sum())