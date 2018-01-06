 
################################################################################                                                                                                                           
#Amin Boroomand 2017
# GOAL: compute the average functional load for each dimention  
#INPUTS:2nd and 3rd functional load ratio
################################################################################
import os
import pandas as pd
from copy import deepcopy
import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt
import glob
import os
from pandas import *

################################################################################  
TrialNum=500         #insert number of trials
GenerNum=21         #insert number of generation
indexlist=[]

med=GenerNum-1
for i in range(TrialNum):
    indx=med+(i*GenerNum)
    indexlist.append(indx)
#print("computing the index of median for each Trial")


WDadrs= '/home/aboroomand/RunILM/bigger/'
os.chdir(WDadrs)
dataList = glob.glob(r'*.tsv')


#reading the file names
nameList = []
dataDct = {}
for lines in dataList:
    path_list = lines.split(os.sep)
    name = path_list
    for filename in name:
        dataDct[filename]=pd.read_csv(filename, sep='\t',  names = ["second","third"]) 


for lines in dataList:
    dictdf=dataDct[lines]  #All data in a file
    line_name=lines[:-41]  #noise rate that extracted from file name
    filename=lines[:-4]
    sec_med=dictdf["second"].median()
    Third_med=dictdf["third"].median()
    
    second_column=dictdf["second"]
    Third_column=dictdf["third"]

    newdf=dictdf.ix[indexlist]
    newdf.to_csv(filename+'_final_FL_t500_G21.tsv', sep='\t', index=None, header=None)
    sec_med=newdf["second"].median()
    Third_med=newdf["third"].median()
    
    print("Noise rate= ",line_name, "    median 2nd dimension= ", sec_med,"   median 3rd dimension=", Third_med)

