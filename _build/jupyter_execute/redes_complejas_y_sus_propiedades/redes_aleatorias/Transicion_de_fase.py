#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import datetime


# In[ ]:


hora = datetime.datetime.now().time()
print('Hora de inicio: %s:%s:%s'%(str(hora.hour).zfill(2), str(hora.minute).zfill(2), str(hora.second).zfill(2)))

inicio = datetime.datetime.now()
corridas = [1000, 100, 10, 1, 1]
dominio = np.logspace(-6,0)
N = [10, 100, 1000, 10000, 100000]

Y = []
for i in range(3):
    #N = N[i]
    Ndep = []
    print('Red N = ',N[i])
    for prob in dominio:
        Ns = []
        for j in range(corridas[i]):
            G = nx.random_graphs.gnp_random_graph(n=N[i], p = prob)
            Ns.append( len(max(list(nx.connected_components(G)), key=len)) )
        Ndep.append(np.mean(Ns))
    Y.append(Ndep)
    tiempo = (datetime.datetime.now() - inicio).seconds
    print(N[i],'nodos: tiempo de cálculo ', tiempo)


for i in [3,4]:
    Ndep = []
    alerta = 0
    print('Red N = ',N[i])
    for prob in dominio:
        print('probabilidad = ',prob)
        Ns = []
        for j in range(corridas[i]):
            G = nx.random_graphs.gnp_random_graph(n=N[i], p = prob)
            Ns.append( len(max(list(nx.connected_components(G)), key=len)) )
        Ndep.append(np.mean(Ns))
        if Ndep[-1] >= .95*N[i]:
            alerta +=1
            print('alerta: ',alerta)
        if alerta == 5:
            break
    Y.append(Ndep)
    tiempo = (datetime.datetime.now() - inicio).seconds
    print(N[i],'nodos: tiempo de cálculo ', tiempo)


# In[ ]:


#Y.append(Ndep)
#tiempo = (datetime.datetime.now() - inicio).seconds
#print(N[i],'nodos: tiempo de cálculo ', tiempo)


# In[ ]:


Ns = [10, 100, 1000, 10000, 100000]
plt.figure(figsize = [15,5])
for i in range(5):  
    ks = dominio*(Ns[i]-1)
    plt.plot(dominio[:len(Y[i])], np.array(Y[i])/Ns[i], '-o', label = 'N = '+str(Ns[i]))    
plt.xscale('log')
plt.legend()


# In[ ]:


Ns = [10, 100, 1000, 10000, 100000]
plt.figure(figsize = [15,5])
for i in range(5):  
    #ks = dominio*(Ns[i]-1)
    #plt.plot(ks, np.array(Y[i])/Ns[i], '-', label = Ns[i])
    ks = dominio*(Ns[i]-1)
    plt.plot(ks[:len(Y[i])], np.array(Y[i])/Ns[i], '-.', label = 'N = '+str(Ns[i]))
plt.xscale('log')
plt.legend()
plt.xlim(10**(-2),10**2)

