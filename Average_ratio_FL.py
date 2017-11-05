 
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
WDadrs= '/home/aboroomand/ILMresults/'
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
    dictdf=dataDct[lines]
    line_name=lines[:-41]
    sec_med=dictdf["second"].median()
    Third_med=dictdf["third"].median()
    
    print("name  ",line_name, "median sec dim  ", sec_med,"median third dim", Third_med)

