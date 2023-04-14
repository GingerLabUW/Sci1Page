# -*- coding: utf-8 -*-
"""
@author: Yangwei Shi/GingerLab@UW
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

font={'weight' : 'bold',
      'size' : 22,
     'family': 'Tahoma'}
mpl.rc('font',**font)

def PVSK_boxplot(filePath= '', fileName = '',figSize=(8.8,6.6),ylabels = ['$\it{V}_{OC}$ (V)','PCE (%)','$\it{J}_{SC}$ (mA/cm$^2$)','FF (%)'], \
                 device_parameters=['Voc','PCE','Jsc','FF'], FigName = ['Voc','PCE','Jsc','FF'],ylims = [[0.8,1.22],[12,22],[18,24],[60,85]]):
    """
    **This is to generate the boxplot of perovskite solar cell parameters such as Voc, PCE, FF, Jsc**
    !!!attention---you only need to change 1,2,6,7. shouldn't modify other keyworks!!!
    1. filePath:
    2. fileName: without extension, as it is already included in the code
    3. figSize: default value is (8.8,6.6) change this if need
    4. ylabes: default value, should not change
    5. device_parameters: default value, should not change
    6. FigName: this can be changed
    7. ylims: this can be changed to make the boxplot looks better
    
    """
    df = pd.read_csv(filePath+fileName+'.csv')
    
    for i in range(4):
        fig,axs = plt.subplots(figsize=figSize)
        axs=sns.boxplot(x='Sample',y = device_parameters[i], data = df,linewidth=2.5)
        axs=sns.swarmplot(x='Sample', y = device_parameters[i], data= df,color='black')
        axs.set_ylabel(ylabels[i],fontsize=22,fontweight='bold')
        axs.set_xlabel('',fontsize=22,fontweight='bold')
        axs.set_ylim(ylims[i])
        for axis in ['top','bottom','left','right']:
            axs.spines[axis].set_linewidth(3)
            axs.tick_params(direction='in',width=3,length=6)
        plt.tight_layout()
        plt.savefig(filePath+FigName[i], bbox_inches='tight',dpi=300)
    
    
    
    