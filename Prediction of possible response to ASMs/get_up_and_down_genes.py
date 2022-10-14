import pandas as pd
import numpy as np
import csv

###########################################
#### You should change variables below ####
###########################################

YOUR_PATH_TO_DATASETS = "Your path of datasets folder"
PATH_OF_datav2 = "Your path of datav2.csv"

threshold = 1 # fold change threshold

###########################################
#### You should change variables above ####
###########################################



data = pd.read_csv(PATH_OF_datav2, header=0, index_col='id', low_memory=False)
columns = data.columns.values.tolist()
new_columns = []
columns_h = []
columns_VA = []
columns_CBZ = []
columns_PHT = []
columns_naive = []
for column in columns:
    new_columns.append(column.replace(" ", "_"))
    if 'Healthy' in column:
        columns_h.append(column.replace(" ", "_"))
    elif "VA" in column:
        columns_VA.append(column.replace(" ", "_"))
    elif "CBZ" in column:
        columns_CBZ.append(column.replace(" ", "_"))
    elif "PHT" in column:
        columns_PHT.append(column.replace(" ", "_"))
    elif "Drug" in column:
        columns_naive.append(column.replace(" ", "_"))
data.columns = new_columns

h = data.loc[:,columns_h]
VA = data.loc[:,columns_VA]
CBZ = data.loc[:,columns_CBZ]
PHT = data.loc[:,columns_PHT]
naive = data.loc[:,columns_naive]
drug = pd.concat([VA, CBZ, PHT], axis=1)
columns_drug = drug.columns.values.tolist()


lst_naive=['Drug-na?ve_IE-9',
'Drug-na?ve_IE-6',
'Drug-na?ve_IE-5',
'Drug-na?ve_IE-4',
'Drug-na?ve_IE-21',
'Drug-na?ve_IE-19',
'Drug-na?ve_IE-17',
'Drug-na?ve_IE-15',
'Drug-na?ve_IE-14',
'Drug-na?ve_IE-13',
'Drug-na?ve_IE-11',
'Drug-na?ve_IE-10',
'Drug-na?ve_IE-1',]

lst_drug=["VA_Responder-9",
"VA_Responder-8",
"VA_Responder-7",
"VA_Responder-6",
"VA_Responder-5",
"VA_Responder-4",
"VA_Responder-3",
"VA_Responder-2",
"VA_Responder-16",
"VA_Responder-15",
"VA_Responder-14",
"VA_Responder-13",
"VA_Responder-11",
"VA_Responder-10",
'VA_Responder-1GSM4255771',
"VA_Non-responder-9",
"VA_Non-responder-8",
"VA_Non-responder-7",
"VA_Non-responder-6",
"VA_Non-responder-5",
"VA_Non-responder-4",
"VA_Non-responder-2",
"VA_Non-responder-1",
"PHT_Responder-4",
"PHT_Responder-1",
'CBZ_Responder-8',
'CBZ_Responder-5',
'CBZ_Non-responder-9',
'CBZ_Non-responder-4',
]

def compare(health, naive, threshold=0.001):
    UP, DOWN = [], []
    health = health.mean(axis=1)
    up = naive > (health+threshold)
    down = naive < (health-threshold)
    UP = naive[up].index.values.tolist()
    DOWN = naive[down].index.values.tolist()
    return UP, DOWN


def compare2(health, naive, nums=10):
    UP, DOWN = [], []
    health = health.mean(axis=1)
    result = (naive -health).sort_values(ascending=False)
    UP = naive[0:nums].index.values.tolist()
    DOWN = naive[-1-nums:-1].index.values.tolist()
    return UP, DOWN

def fold_change_compare(health, naive, threshold=1, limit_len=False):
    UP, DOWN = [], []
    
    # fold change
    health = np.power(2, health)
    health = health.mean(axis=1)
    health = np.log2(health)
    inter = (naive - health).sort_values(ascending=False)
    
    up = naive >= (health+threshold)
    down = naive <= (health-threshold)
    UP = inter[up].index.values.tolist()
    DOWN = inter[down].index.values.tolist()
    if limit_len:
        if len(UP) >= 150:
            UP = UP[0:150]
        if len(DOWN) >= 150:
            DOWN = DOWN[0:150]
    return UP, DOWN


def sample(df1, df2, n=5,threshold=1):
    
    result = df2.sample(n=n, axis=1)
    result = np.power(2,result)
    result = result.mean(axis=1)
    result = np.log2(result)
    
    for i in range(n-1):
        inter = df2.sample(n=n, axis=1)
        inter = np.power(2,inter)
        inter = inter.mean(axis=1)
        inter = np.log2(inter)
        result = result+inter
        
    df2 = result/n
    up = df1 >= (df2+threshold)
    down = df1 <= (df2-threshold)
    UP = df1[up].index.values.tolist()
    DOWN = df1[down].index.values.tolist()
    return UP, DOWN




if __name__ == "__main__":
    limit_len = False
    dic_up = {}
    dic_down = {}
    naive_sub = naive[lst_naive]
    columns = lst_drug
    

    for column in columns:
        UP, DOWN = fold_change_compare(naive_sub, drug[column], threshold=threshold, limit_len=limit_len)
        dic_up[column]=UP
        dic_down[column]=DOWN
        
    print(len(dic_up))

    with open("./{0}_up.gmt".format(threshold), 'w', newline='\n') as f:
        writer = csv.writer(f, delimiter='\t')
        for column in columns:
            writer.writerow([column+"_UP", "BLACK"]+dic_up[column])
    with open("./{0}_down.gmt".format(threshold), 'w', newline='\n') as f:
        writer = csv.writer(f, delimiter='\t')
        for column in columns:
            writer.writerow([column+"_DN", "BLACK"]+dic_down[column])
            
            
    df = pd.read_csv(YOUR_PATH_TO_DATASETS+r'\l1000\m2.subset.10k\data\splited\health'+'.csv', sep='\t', index_col='id')
    dic_up = {}
    dic_down = {}

    for column in columns_naive:
        UP, DOWN = fold_change_compare(df, naive[column], threshold=threshold, limit_len=limit_len)
        dic_up[column]=UP
        dic_down[column]=DOWN

    with open("./compare_gene/{0}_up.gmt".format(threshold), 'w', newline='\n') as f:
        writer = csv.writer(f, delimiter='\t')
        for column in columns_naive:
            writer.writerow([column+"_UP", "BLACK"]+dic_up[column])
    with open("./compare_gene/{0}_down.gmt".format(threshold), 'w', newline='\n') as f:
        writer = csv.writer(f, delimiter='\t')
        for column in columns_naive:
            writer.writerow([column+"_DN", "BLACK"]+dic_down[column])