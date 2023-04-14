# -*- coding: utf-8 -*-
"""
@author: Yangwei Shi/GingerLab@UW
"""
def pvsk(x,y,M,V):
    """
    formular of perovskite: FAxCs(1-x)Pb(I(1-y)Bry)3
    x: FA mole
    y: Br mole
    M: mole of precursor solution, mole
    V: volume of precursor solution, ml
    """
    # molecular weight of precursors
    CsI = 259.81 # g/mol
    FAI = 171.91 # g/mol
    PbI2 = 461.01 # g/mol
    PbBr2 = 367.01 # g/mol
    
    w_FAI = x*FAI*M*V
    print("FAI:%.3f"% w_FAI,'mg')
    w_CsI = (1-x) *CsI*M*V
    print("CsI: %.3f"% w_CsI,'mg')
    w_PbI = (3*(1-y)-1)/2*PbI2*M*V
    print("PbI2:%.3f"% w_PbI,'mg')
    w_PbBr = 3*y/2*PbBr2*M*V           
    print("PbBr2:%.3f"% w_PbBr,'mg')
    return

