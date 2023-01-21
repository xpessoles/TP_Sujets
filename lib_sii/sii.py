# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 15:14:58 2023

@author: xpess
"""

import numpy as np
import matplotlib.pyplot as plt

def trapeze_vitesse(xi:float, xf:float, vmax:float, amax:float, dt:float) -> np.ndarray :
    """
    Calcule les profils de profils de position, vitesse et accélération. 

    Parameters
    ----------
    xi,xf : float 
        abscisse de départ, abscisse d'arrivée (m, mm ou rad).
    vmax : float
        vitesse maximale atteignable (m/s, mm/s ou rad/s).
    amax : float
        accélérationmaximale atteignable (m/s², mm/s² ou rad/s²).
    dt : float
        incrément de temps en s.
    Returns
    -------
    les_t, les_x, les_v, les_a.

    """ 
    
    ## Calcul du temps des différentes phases
    ## On vérifie que la vitesse vmax est atteignable
    
    # Temps d'accélération : # ta = vmax/amax
    # Calcul de la distance minimale pour atteindre la vitesse
    dmini = vmax*vmax/amax   # dmini = ta*vmax 
    
    # Si la distance à parcourir est inférieure à la distance minimale
    # On aura un profil de vitesse en triangle
    if abs(xf - xi) < dmini : 
        # On calcule la vitesse atteignable:
        vmax = (abs(xf - xi)*amax)**.5
        ta = vmax / amax
        T = 0
    else : 
        ta = vmax / amax
        # Calcul du temps à vitesse constante: 
        D = abs(xf - xi)
        # Aire sous la courbe de vitesse: D = vmax*ta + T*vmax
        T = (D - vmax*ta)/vmax
    
    t = 0
    les_t,les_x,les_v,les_a = [],[],[],[]
    if xi>xf :
        amax = -amax
        vmax = -vmax
    
    while t <= 2*ta+T+100*dt: # On simule sur n*dt de plus que la durée du mouvement
        if t < ta :
            les_t.append(t)
            les_a.append(amax)
            les_v.append(amax*t)
            les_x.append(0.5*amax*t*t)
        elif t< ta+T :
            les_t.append(t)
            les_a.append(0)
            les_v.append(vmax)
            les_x.append(les_x[-1]+vmax*dt)
        elif t < 2*ta+T : 
            les_t.append(t)
            les_a.append(-amax)
            les_v.append(les_v[-1]-amax*dt)
            les_x.append(les_x[-1]+les_v[-1]*dt)
        else : 
            les_t.append(t)
            les_a.append(0)
            les_v.append(0)
            les_x.append(les_x[-1])
        t=t+dt
    return les_t, les_x, les_v, les_a

def read_from_tracker(file:str) :
    """
    Parsing des données provenant du logiciel de pointage Tracker sur 3 colonnes :
    temps,abscisse,ordonnée
    On supprime les deux premières lignes qui contiennent des informations sur les colonnes.
    On supprime les mesures qui ont échouées lors du tracking.


    Parameters
    ----------
    file : str
        nom du fichier texte (et lien).

    Returns
    -------
    (list,list,list)
        Valeurs expérimentales : les_temps, les_x, les_y

    """
    fid = open(file,"r")  
    data = fid.readlines()
    fid.close()
    data = data[2:]
    les_t_exp, les_x_exp, les_y_exp = [],[],[]
    for ligne in data[:-1] : 
        l = ligne.split("\t")
        if len(l[0])>4 and len(l[1])>4 and len(l[2])>4 :
            les_t_exp.append(float(l[0].replace(",",'.')))
            les_x_exp.append(float(l[1].replace(",",'.')))
            les_y_exp.append(float(l[2].replace(",",'.')))
    return les_t_exp, les_x_exp, les_y_exp
    
def test_trapeze():
    les_t, les_x, les_v, les_a = trapeze_vitesse(0, -100, 0.5*100, 5*100, 0.001)
    plt.plot(les_t,les_a)
    plt.plot(les_t,les_v)
    plt.plot(les_t,les_x)
    plt.grid()
    plt.show()
    


