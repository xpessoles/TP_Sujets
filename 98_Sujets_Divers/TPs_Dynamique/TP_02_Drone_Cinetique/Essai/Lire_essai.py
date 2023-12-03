import numpy as np
import matplotlib.pyplot as plt


fid = open("TestPendule.csv")
data = fid.readlines()
fid.close()

les_t=[]
les_angles=[]
data = data[2:]
for ligne in data:
    ligne  =ligne.split(";")
    les_t.append(float(ligne[0]))
    les_angles.append(float(ligne[1]))
    
# Conversion des angles
for i in range(len(les_angles)):
    les_angles[i]=les_angles[i]*0.0055-0.11#+0.0899


plt.plot(les_t,les_angles)
plt.grid()
plt.show()

