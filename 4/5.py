
# coding: utf-8

# In[51]:

path = 'F:\\UCSD\\AI\\4\\'

f = open(path+'nasdaq00.txt', 'r')
data1 = [float(i.split()[0]) for i in f.readlines()]
f = open(path+'nasdaq01.txt', 'r')
data2 = [float(i.split()[0]) for i in f.readlines()]


# In[52]:

import numpy as np
prev = 4
xt = np.zeros(prev)
A = np.zeros((prev,prev))
B = np.zeros(prev)

for i in xrange(prev, len(data1)):
    xt = data1[i-prev:i]
    at = np.outer(xt,xt)
    A += at
    bt = np.dot(data1[i], xt)
    B += bt
    
weights = np.dot(np.linalg.inv(A), np.transpose(B))
    


# In[53]:

weights


# In[35]:

yt = np.zeros(len(data1) - prev)
xxt = np.zeros(prev)
for i in xrange(prev, len(data1)):
    xxt = data1[i-prev:i]
    yt[i-prev] = np.dot(xxt, weights)

trainerror = (yt - data1[prev:len(data1)])**2
np.mean(trainerror)


# In[46]:

yyt = np.zeros(len(data2))
xxt = data1[-1*prev:]

for i in xrange(prev):
    xxxt = xxt[i:prev] + data2[0:i]
    yyt[i] = np.dot(xxxt,weights)

for i in xrange(prev, len(data2)):
    xxxt = data2[i-prev:i]
    yyt[i] = np.dot(xxxt, weights)

testerror = (yyt - data2)**2
np.mean(testerror)


# In[ ]:

# I would recommend this linear model for stock market prediction. predicted values are close to the given labels.

