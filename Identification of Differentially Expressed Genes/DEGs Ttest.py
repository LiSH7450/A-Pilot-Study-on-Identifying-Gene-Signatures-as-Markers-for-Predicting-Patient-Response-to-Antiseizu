# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd
from scipy import stats

filepath1 = 'VARe_I.xlsx'
filepath2 = 'VANon_I.xlsx'
filepath8 = 'drugnaive_I.xlsx'
VARe_I = pd.read_excel(filepath1,index_col=0)
VANon_I = pd.read_excel(filepath2,index_col=0)
drugnaive_I = pd.read_excel(filepath8,index_col=0)

filepath='gene list.xlsx'
gene = pd.read_excel(filepath)
deg=gene['ID']

VARe_I=VARe_I[deg]
VANon_I=VANon_I[deg]
drugnaive_I=drugnaive_I[deg]


R=[]
for i in deg:
    pVal = stats.ttest_ind(VARe_I[i], drugnaive_I[i], equal_var=True)
    R.append(pVal)
R = np.array(R)

N=[]

for i in deg:
    pVal = stats.ttest_ind(VANon_I[i],drugnaive_I[i], equal_var=True)
    N.append(pVal)
N = np.array(N)  
    
RN=[]

for i in deg:
    pVal = stats.ttest_ind(VARe_I[i],VANon_I[i], equal_var=True)
    RN.append(pVal)
RN = np.array(RN)    
    
# pd.DataFrame(R[:, 1]).to_csv('R_pval.csv')
# pd.DataFrame(N[:, 1]).to_csv('N_pval.csv')
# pd.DataFrame(RN[:, 1]).to_csv('RN_pval.csv')