
# coding: utf-8

# In[1]:

import numpy as np
path = 'F:\\UCSD\\AI\\5\\'

f = open(path+'spectY.txt','r')
Y = np.array([int(i.split()[0]) for i in f.readlines()])
f.close()

f = open(path+'spectX.txt','r')
X = np.array([[int(j) for j in i.split()] for i in f.readlines()])
f.close()


# In[3]:

n = len(X[0])
T = len(X)

p = np.array([2.0/n]*n)
Ti = X.sum(axis=0)
check = 1
for j in xrange(257):
    
    L = 0
    M=0
    for t in xrange(T):
 
        temp = np.power((np.array([1]*n) - p),X[t])
        prediction = (1-temp.prod())

        if (Y[t]==0 and prediction >= 0.5) or (Y[t]==1 and prediction <= 0.5):
            M += 1

        if Y[t] == 0:
            L+=np.log(1-prediction)
        else:
            L+=np.log(prediction)

    if j==0 or j%check == 0:
        print 'iterations :', j
        print 'errors :', M
        print 'L :', (1.0/T)*L
        if j!=0:
            check *= 2
    
    newp = np.zeros(n)
    
    for t in xrange(T):

        temp = np.power((np.array([1]*n) - p),X[t])
        denominator = (1-temp.prod())

        for i in xrange(n):

            numerator = Y[t]*X[t][i]*p[i]
            newp[i] += (numerator/denominator)

    p = newp/Ti


# In[ ]:



