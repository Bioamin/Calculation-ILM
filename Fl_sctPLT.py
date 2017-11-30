

################################################################################
#Amin Boroomand 2017
# GOAL: make scatter plot for Functional load                                                                                                                                                   
#INPUTS:2nd and 3rd functional load for 100 chain
#OUTPUTS:scatter plot 
#################################################################################
import os
import pandas as pd
from copy import deepcopy
import numpy as np
import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import glob

################################################################################

WDadrs= '/home/aboroomand/ILMresults/100t_21G/'
os.chdir(WDadrs)
dataList = glob.glob(r'*.tsv')
No_nise_dataList = glob.glob(r'*.csv')

nameList = []
dataDct = {}

def importfile (FLfile,line_name,Nonoisefile , WDadrs= '/home/aboroomand/ILMresults/100t_21G/'):

    noise_percent=line_name,
    funcLoad= pd.read_csv(FLfile, sep='\t',  names = ["second","third"])
    Nonoisefile= pd.read_csv(Nonoisefile, sep='\t', names = ["second","third"])
    sLength = len(funcLoad['second'])
    noise=float(line_name)
    L = [noise for i in range(sLength)]
    L=pd.Series(L)
    funcLoad = pd.concat([funcLoad, L.rename("noise")], axis=1)

    Nonoise=0.0
    NNlenth=len(Nonoisefile['third'])
    CL=[Nonoise for i in range(NNlenth)]
    CL=pd.Series(CL)
    Nonoisefile=pd.concat([Nonoisefile,CL.rename("noise")], axis=1)
    
    frames = [funcLoad,Nonoisefile]
    FL_data = pd.concat(frames,keys=['WN', 'NN'])
    return FL_data,noise_percent

def scrtPLT (FL_data,noise_percent,savingpath="/home/aboroomand/ILMresults/100t_21G/"):
    cond = FL_data.noise > 0.0
    subset_a = FL_data[cond].dropna()
    subset_b = FL_data[~cond].dropna()
    plt.scatter(subset_a.second, subset_a.third, s=20, c='b', label=noise_percent+'% Noise in Middle Vowel')
    plt.scatter(subset_b.second, subset_b.third, s=20, c='r', label='without noise')
    plt.xlabel('Functional Load on Middle Vowel', fontsize=20)
    plt.ylabel('Functional Load on Final Consonant', fontsize=20)
    plt.axis('equal')
    plt.legend()
    plt.show()
    plt.savefig(savingpath +noise_percent+"_Functional_load_sccaterPLT.png")
    #plt.hold(False)
    plt.close()
    return()

def main (line_name,FLfile,Nonoisefile,savingpath="/home/aboroomand/ILMresults/100t_21G/" ):
    FL_data,noise_percent =importfile (FLfile ,line_name,noNoisefile)
    scrtPLT (FL_data, line_name,savingpath="/home/aboroomand/ILMresults/100t_21G/")
    return

for lines, noNoisefile in zip(dataList, No_nise_dataList):
    
    line_name=lines[:-60]
    FLfile=lines
    FL_data,noise_percent =importfile (FLfile ,line_name, noNoisefile)
    scatterfile=main (line_name, FLfile= lines , Nonoisefile=noNoisefile, savingpath="/home/aboroomand/ILMresults/100t_21G/")
