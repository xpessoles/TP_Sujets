# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 15:14:58 2023

@author: xpess
"""

import numpy as np

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
        
        
    deltax = xf - xi
    
    10 > 1
    