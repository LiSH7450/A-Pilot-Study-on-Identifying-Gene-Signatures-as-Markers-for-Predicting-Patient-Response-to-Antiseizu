# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd
from scipy import stats

filepath1 = 'VARe_I.xlsx'
filepath2 = 'VANon_I.xlsx'
filepath3 = 'drugnaive_I.xlsx'

#1
VARe_I = pd.read_excel(filepath1,index_col=0)
VANon_I = pd.read_excel(filepath2,index_col=0)
drugnaive_I = pd.read_excel(filepath3,index_col=0)


VARe_I = np.log2(VARe_I+1)
VANon_I = np.log2(VANon_I+1)
drugnaive_I = np.log2(drugnaive_I+1)


pVals = []
for i in range(VARe_I.shape[1]):
    pVal = stats.ttest_ind(VARe_I.iloc[:, i], drugnaive_I.iloc[:, i], equal_var=True)
    pVals.append(pVal)
pVals = np.array(pVals)
print('after TT, %d least' % (((pVals[:, 1] < 0.05).squeeze()).sum()))

VARe_I.loc['pvalue',:]=pVals[:, 1]
VARe_I = VARe_I.T
VARe_I.to_csv('VARe_I_PVAL.csv')


pVals = []
for i in range(VANon_I.shape[1]):
    pVal = stats.ttest_ind(VANon_I.iloc[:, i], drugnaive_I.iloc[:, i], equal_var=True)
    pVals.append(pVal)
pVals = np.array(pVals)
print('after TT, %d least' % (((pVals[:, 1] < 0.05).squeeze()).sum()))

VANon_I.loc['pvalue',:]=pVals[:, 1]
VANon_I = VANon_I.T
VANon_I.to_csv('VANon_I_PVAL.csv')