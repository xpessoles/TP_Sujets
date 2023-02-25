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
    
def plot_4_mesures(HG:str,HD:str,BG:str,BD:str):
    les_index_hg,les_t_hg,les_c1_hg,les_c2_hg,les_c3_hg,les_c4_hg,les_col_hg = read_from_rc4(HG)
    les_index_hd,les_t_hd,les_c1_hd,les_c2_hd,les_c3_hd,les_c4_hd,les_col_hd = read_from_rc4(HD)
    les_index_bg,les_t_bg,les_c1_bg,les_c2_bg,les_c3_bg,les_c4_bg,les_col_bg = read_from_rc4(BG)
    les_index_bd,les_t_bd,les_c1_bd,les_c2_bd,les_c3_bd,les_c4_bd,les_col_bd = read_from_rc4(BD)
file_hg = "RC4/01_HG.csv"
file_hd = "RC4/01_HD.csv"
file_bg = "RC4/01_BG.csv"
file_bd = "RC4/01_BD.csv"
    
#plot_file(file_hg)




