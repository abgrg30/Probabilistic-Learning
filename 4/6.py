
# coding: utf-8

# In[173]:

#Gradient Ascent using Sigmoid


# In[179]:

path = 'F:\\UCSD\\AI\\4\\'

f = open(path+'newTrain3.txt', 'r')
data1 = [[int(j) for j in i.split()] for i in f.readlines()]
f = open(path+'newTrain5.txt', 'r')
data2 = [[int(j) for j in i.split()] for i in f.readlines()]


# In[180]:

import math
import numpy as np

def sigmoid(x):
    return 1 / (1 + math.exp(-x))


# In[181]:

training = data1 + data2
yt = [1]*len(data1) + [0]*len(data2)


# In[182]:

def errorcalc(training,wt,yt,iterations,s):
    trainerror=0
    predicttrain = np.zeros(len(training))

    for i in xrange(len(training)):
        sig = sigmoid(np.dot(wt, training[i]))

        if sig > 0.5:
            predicttrain[i] = 1
        if predicttrain[i] != yt[i]:
            trainerror +=1
            
    print '%s Error : %f' %(s, float(trainerror)/len(training)*100)


# In[183]:

#wt = np.zeros(len(training[0]))
wt = np.random.uniform(0, 1, len(training[0]))

eta = 0.2/len(training)
CONVERGENCE=0.001
checkafteriteration = 500 #1000

iterations=0
prevtrainlikelihood = 0

while 1:    
    
    gradient = np.zeros(len(training[0]))
    
    for i in xrange(len(training)):
        sig = (yt[i] - sigmoid(np.dot(wt, training[i])))
        gradient += np.dot(sig, training[i])   
        
    wt = wt + (eta * gradient)
    iterations +=1
    
    trainlikelihood = 0
    for i in xrange(len(training)):
        sig = sigmoid(np.dot(wt, training[i]))
        trainlikelihood += np.log(yt[i]*sig + (1-yt[i])*(1-sig))
        
    if ((trainlikelihood - prevtrainlikelihood)) < CONVERGENCE and iterations != 1:   
        break   
    
    prevtrainlikelihood = trainlikelihood
    
    if(iterations%checkafteriteration == 0):        
        print '%s Likelihood after %d iterations : %f' %('Training', iterations, trainlikelihood)
        errorcalc(training,wt,yt,iterations,'Training')


# In[184]:

print 'Final Result'
print ''
print '%s Likelihood after %d iterations : %f' %('Training', iterations, trainlikelihood)

errorcalc(data1,wt,[1]*len(data1),iterations,'Training3')
errorcalc(data2,wt,[0]*len(data2),iterations,'Training5')
errorcalc(training,wt,yt,iterations,'Training')


# In[185]:

f = open(path+'newTest3.txt', 'r')
data3 = [[int(j) for j in i.split()] for i in f.readlines()]

testlabels = [1]*len(data3)
errorcalc(data3,wt,testlabels,iterations,'Test3')

f = open(path+'newTest5.txt', 'r')
data4 = [[int(j) for j in i.split()] for i in f.readlines()]

testlabels = [0]*len(data4)
errorcalc(data4,wt,testlabels,iterations,'Test5')

test = data3 + data4
testlabels = [1]*len(data3) + [0]*len(data4)

errorcalc(test,wt,testlabels,iterations,'Test')


# In[186]:

arr = np.reshape(wt, (8,8))
print arr

