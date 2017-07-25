# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import math
def trignometric_expansion(data, k):
    l = [data]
    cols = data.columns
    for j in range(1, k+1):
        cos = np.cos(j*math.pi*data)
        cos.columns = [(cols[i] + '_cos{0}pi'.format(j)) for i in range(len(cols))]
        sin = np.sin(j*math.pi*data)
        sin.columns = [(cols[i] + '_sin{0}pi'.format(j)) for i in range(len(cols))]
        l.append(cos)
        l.append(sin)
    output = pd.concat(l, axis=1)
    output.dropna(axis=0, how='any', inplace=True)
    return output
def chebyshev_expansion(data, k):
    l = []
    l.append(data)
    l.append(2*data*data - 1)
    cols = data.columns
    for j in range(k-1):      
        new = 2*data*l[-1]-l[-2]
        l.append(new)
    for j in range(1, k + 1):
        l[j].columns = [(cols[i] + '_che{0}'.format(j)) for i in range(len(cols))]
    output = pd.concat(l, axis=1)
    output.dropna(axis=0, how='any', inplace=True)
    return output
def legendre_expansion(data, k):
    l = []
    l = []
    l.append(data)
    l.append((3*data*data - 1)/2)
    cols = data.columns
    for j in range(3,k+2):      
        new = ((2*j-1)*data*l[-1] - (j-1)*l[-2])/j
        l.append(new)
    for j in range(1, k + 1):
        l[j].columns = [(cols[i] + '_che{0}'.format(j)) for i in range(len(cols))]
    output = pd.concat(l, axis=1)
    output.dropna(axis=0, how='any', inplace=True)
    return output

def inter_polation_norm_0_1(x):
    return (x-x.min())/(x.max() - x.min())
def inter_polation_norm_1_1(x):
    return 2*(x-x.min())/(x.max() - x.min()) - 1
def z_score_norm(x):
    return (x - x.mean())/x.std()
def step(x):
    return 1*(x>0)
def new_inter_polation_norm_1_1(x):
    return (x-2*x.min())/(x.max() - 2*x.min())
        