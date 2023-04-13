# -*- coding: utf-8 -*-
"""
@author: Yangwei Shi/GingerLab
""" 
from igor import binarywave as bw
import matplotlib.pyplot as plt
import matplotlib as mpl

def SKPM_plot(filePath = '', fileName='', scale = 4, cmap='magma', clim = [90,120],FigName='SKPM.png'):
    """
    ---This is for plotting the SKPM image, potential part---
    1. filePath: complete file path
    2. fileName: filename without extension as extension .ibw has been attached inside of the code
    3. cmap = cmap
    4. scale: image size, i.g. 4um x 4um just type 4, by the way, the defalt pixel in x axis is 256
       the default scale is set to 1 um
    5. clim: colorbar range, based on the raw image, change this range
    6. FigName = FigName
    """
    
    font={'weight' : 'bold',
      'size' : 22,
     'family': 'Tahoma'}
    mpl.rc('font',**font)
    
    folder = filePath
    df = bw.load(folder + fileName +'.ibw')
    df_skpm = df['wave']['wData']
    df_potential = df_skpm[:,:,3]*1000
   
    
    fig,axs = plt.subplots(figsize=(8,6))
    plt.imshow(df_potential,cmap=cmap)
    # costimize colobar
    cbar=plt.colorbar()
    cbar.mappable.set_clim(90,120)  # Range
    cbar.set_label('Potential (mV)', rotation=270, fontsize=20, fontweight='bold',labelpad=18) #labelpad=20
    cbar.outline.set_linewidth(3)
    cbar.ax.tick_params(width=3,labelsize=20)
    plt.tight_layout()
    plt.xticks([])
    plt.yticks([])
    
    # draw a scale
    scale = scale # um
    x = [245-256/(scale), 245] # 1 um,
    y = [245, 245]
    plt.plot(x, y, color="white", linewidth=6.5)
    
    # change the outline thickness
    for axis in ['top','bottom','left','right']:
        axs.spines[axis].set_linewidth(3)
        axs.tick_params(direction='in',width=3,length=6)
    plt.tight_layout()
    # save figure
    plt.savefig(folder + FigName, bbox_inches='tight', dpi=300)
    
    
    
    
    
    
    
    
    
    