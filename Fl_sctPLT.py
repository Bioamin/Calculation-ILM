

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


################################################################################
def importfile (FLfile='1.5_noise_slides_2nd_3rd_functional_load.tsv',Nonoisefile="no_noise_slides_2nd_3rd_functional_load.tsv" , WDadrs= '/home/aboroomand/ILMresults/'):
    print("importfile")
    os.chdir(WDadrs)
    funcLoad= pd.read_csv(FLfile, sep='\t',  names = ["second","third"])
    Nonoisefile= pd.read_csv(Nonoisefile, sep='\t', names = ["second","third"])
    sLength = len(funcLoad['second'])
    noise=1.5
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
    #A = funcLoad[funcLoad.label == 1]


    
    #print(Nonoisefile)
    #print(Nonoisefile)
    #funcLoad['noise']=Series(np.noise(sLength), index=funcLoad.index)
    #print(FL_data)
    return FL_data


def scrtPLT (FL_data,savingpath="/home/aboroomand/ILMresults/"):
    cond = FL_data.noise > 0.0
    subset_a = FL_data[cond].dropna()
    subset_b = FL_data[~cond].dropna()
    print(subset_a.second)
    plt.scatter(subset_a.second, subset_a.third, s=20, c='b', label='15% Noise in Middle Vowel')
    plt.scatter(subset_b.second, subset_b.third, s=20, c='r', label='without noise')




    #plt.scatter(FL_data['2nd'], FL_data['3rd'])
    plt.xlabel('Functional Load on Middle Vowel', fontsize=20)
    plt.ylabel('Functional Load on Final Consonant', fontsize=20)
    plt.axis('equal')
    plt.legend()
    plt.show()
    plt.savefig(savingpath +"Functional_load_sccaterPLT.png")
    return


def main (FLfile='1.5_noise_slides_2nd_3rd_functional_load.tsv',Nonoisefile="no_noise_slides_2nd_3rd_functional_load.tsv" , WDadrs= '/home/aboroomand/ILMresults/'):
    FL_data=importfile (FLfile='1.5_noise_slides_2nd_3rd_functional_load.tsv' , WDadrs= '/home/aboroomand/ILMresults/')
    scrtPLT (FL_data)
    return
main()
