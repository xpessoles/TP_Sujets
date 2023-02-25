# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 11:39:58 2023

@author: xpess
"""

import numpy as np
import matplotlib.pyplot as plt

def read_from_rc4(file:str):
    fid = open(file,'r')
    data = fid.readlines()
    fid.close()
    
    # On cherche le début et la fin des mesures
    i_deb,i_fin = 0,0
    for i in range(len(data)):
        if "MESURES" in data[i]:
            i_deb = i
        if "Param" in data[i]:
            i_fin = i
    
    les_tit = data[i_deb+1].split(";")
    les_uni = data[i_deb+2].split(";")
    les_col = [les_tit[i]+" ("+les_uni[i]+")" for i in range(len(les_tit))]
    i_deb = i_deb + 3
    i_fin = i_fin -2
    
    
    les_index,les_t,les_c1,les_c2,les_c3,les_c4 = [],[],[],[],[],[]
    
    for i in range(i_deb,i_fin+1):
        ligne = data [i]
        ligne = ligne.replace(",",".")
        ligne = ligne.split(";")
        les_index.append(int(ligne[0]))
        les_t.append(float(ligne[1]))
        if ligne[2] != "": les_c1.append(float(ligne[2])) #else : les_c1.append(0)
        les_c2.append(float(ligne[3]))
        les_c3.append(float(ligne[4]))
        les_c4.append(float(ligne[5]))
    return les_index,les_t,les_c1,les_c2,les_c3,les_c4,les_col


def plot_file(file):
    les_index,les_t,les_c1,les_c2,les_c3,les_c4,les_col = read_from_rc4(file)
    
    #plt.plot(les_t,les_c2,label=les_col[3])
    #plt.plot(les_t,les_c3,label=les_col[4])
    plt.plot(les_t,les_c4,label=les_col[5])
    plt.legend()
    
    plt.grid()
    plt.show()
    
def plot_4_mesures(HG:str,HD:str,BG:str,BD:str,qc:bool):
    """
    

    Parameters
    ----------
    HG : str
        DESCRIPTION.
    HD : str
        DESCRIPTION.
    BG : str
        DESCRIPTION.
    BD : str
        DESCRIPTION.
    qc : bool
        DESCRIPTION.

    Returns
    -------
    None.

    """
    les_index_hg,les_t_hg,les_c1_hg,les_c2_hg,les_c3_hg,les_c4_hg,les_col_hg = read_from_rc4(HG)
    les_index_hd,les_t_hd,les_c1_hd,les_c2_hd,les_c3_hd,les_c4_hd,les_col_hd = read_from_rc4(HD)
    les_index_bg,les_t_bg,les_c1_bg,les_c2_bg,les_c3_bg,les_c4_bg,les_col_bg = read_from_rc4(BG)
    les_index_bd,les_t_bd,les_c1_bd,les_c2_bd,les_c3_bd,les_c4_bd,les_col_bd = read_from_rc4(BD)

    if not qc :
        les_c2_hg = [e/52 for e in les_c2_hg]
        les_c3_hg = [e/52 for e in les_c3_hg]
        les_c2_hd = [e/52 for e in les_c2_hd]
        les_c3_hd = [e/52 for e in les_c3_hd]
        les_c2_bg = [e/52 for e in les_c2_bg]
        les_c3_bg = [e/52 for e in les_c3_bg]
        les_c2_bd = [e/52 for e in les_c2_bd]
        les_c3_bd = [e/52 for e in les_c3_bd]
        les_col_hg[3] = les_col_hg[3].replace("qc","mm")
        les_col_hg[4] = les_col_hg[4].replace("qc","mm")
        les_col_hd[3] = les_col_hd[3].replace("qc","mm")
        les_col_hd[4] = les_col_hd[4].replace("qc","mm")
        les_col_bg[3] = les_col_bg[3].replace("qc","mm")
        les_col_bg[4] = les_col_bg[4].replace("qc","mm")
        les_col_bd[3] = les_col_bd[3].replace("qc","mm")
        les_col_bd[4] = les_col_bd[4].replace("qc","mm")
        
    fig, ax = plt.subplots(nrows=2, ncols=2)#, sharey=True)
    
    # plots
    ax[0][0].plot(les_t_hg, les_c2_hg,label=les_col_hg[3])
    ax[0][0].plot(les_t_hg, les_c3_hg,label=les_col_hg[4])
    
    ax[0][1].plot(les_t_hd, les_c2_hd,label=les_col_hd[3])
    ax[0][1].plot(les_t_hd, les_c3_hd,label=les_col_hd[4])
    
    ax[1][0].plot(les_t_bg, les_c2_bg,label=les_col_bg[3])
    ax[1][0].plot(les_t_bg, les_c3_bg,label=les_col_bg[4])
    
    ax[1][1].plot(les_t_bd, les_c2_bd,label=les_col_bd[3])
    ax[1][1].plot(les_t_bd, les_c3_bd,label=les_col_bd[4])
    
    # labels
    # ax[0][0].set_ylabel('f(x)')
    # ax[0][0].set_xlabel('x')
    # ax[0][1].set_ylabel('g(x)')
    # ax[0][1].set_xlabel('x')
    ax[0][0].legend()
    ax[0][1].legend()
    ax[1][0].legend()
    ax[1][1].legend()
    
    # Grilles
    ax[0][0].grid()
    ax[0][1].grid()
    ax[1][0].grid()
    ax[1][1].grid()
    
    # adjust right subfigure axes location
    # ax[0][1].yaxis.tick_right()
    # ax[0][1].yaxis.set_label_position("right")
    
    # figure settings
    #fig.suptitle('These are some functions', fontsize=16)
    #fig.tight_layout()
    #fig.subplots_adjust(top=0.85) # tight_layout ignores overall titles (current bug
    plt.show()
    plt.close()
    
file_hg = "RC4/01_HG.csv"
file_hd = "RC4/01_HD.csv"
file_bg = "RC4/01_BG.csv"
file_bd = "RC4/01_BD.csv"
    
plot_4_mesures(file_hg, file_hd, file_bg, file_bd,False)
# - Résolution Enrouleur : 52 qc (points codeur) pour 1 mm de câble.
#plot_file(file_hg)




