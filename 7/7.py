
# coding: utf-8

# In[3]:

import numpy as np
import string

path = 'F:\\UCSD\\AI\\7\\'

def readfile(filename):
    global path
    f = open(path + filename, 'r')
    a = np.array([map(float, i.split()[:3]) for i in f.readlines()])
    f.close()
    return a
    
a1 = readfile('prob_a1.txt')
a2 = readfile('prob_a2.txt')
a3 = readfile('prob_a3.txt')
a4 = readfile('prob_a4.txt')

gamma = 0.9875
ns = 81

f = open(path + 'rewards.txt', 'r')
r = np.array([float(i.split()[0]) for i in f.readlines()])
f.close()


# In[4]:

#value iteration

v = np.zeros(ns)
vnew = np.zeros(ns)
pi = np.zeros(ns,dtype=int)
iterator = 0

while 1:
    for s in xrange(ns):
        sum1=0.0
        sum2=0.0
        sum3=0.0
        sum4=0.0
        for row in range(int(a1.shape[0])):
            if (s == (int(a1[row][0])-1)):
                sum1 += a1[row][2]*v[int(a1[row][1])-1]
            if (s == (int(a2[row][0])-1)):
                sum2 += a2[row][2]*v[int(a2[row][1])-1]
            if (s == (int(a3[row][0])-1)):
                sum3 += a3[row][2]*v[int(a3[row][1])-1]
            if (s == (int(a4[row][0])-1)):
                sum4 += a4[row][2]*v[int(a4[row][1])-1]
        
        vnew[s] = r[s] + gamma*max([sum1, sum2, sum3, sum4])
        pi[s] = np.argmax([sum1, sum2, sum3, sum4])
        
    iterator += 1
    if np.equal(vnew,v).all():
        break
    else:
        np.copyto(v,vnew)


# In[5]:

directions = []
movement = []
moves = ['W','N','E','S']
direc = ['<','^','>','v']

for s in xrange(ns):
    movement.append(moves[pi[s]])
    directions.append(direc[pi[s]])


# In[8]:

f = open(path + 'position.txt', 'r')
pos = [map(int, i.split()[:2]) for i in f.readlines()]
f.close()


# In[13]:

print ' 7.2(a) \n'
print 'V*(s) = '
vv = vnew.reshape((9,9))
print np.around(vv.T, 3)
m = np.reshape(movement, (9,9)).T
d = np.reshape(directions, (9,9)).T
pii = pi.reshape((9,9))+1
flag = False

listprint = []
for i in xrange(9):
    for j in xrange(9):
        
        if vv[i][j] > 0:
            listprint.append(((i*9)+j+1, vv[i][j]))
        
        for k in pos:
            if ((k[0]==i) and (k[1]==j)):
                flag = True
                break
                
        if (flag == False):
            d[i][j] = '.'
            m[i][j] = '.'
        else:
            if ((i==6) and (j==8)):
                d[i][j] = 'X'
                m[i][j] = 'X'
                
            flag = False
            
for i in listprint:
    print 'Value at pos %d : %f' %(i[0],i[1])    
    
print '\n 7.2(b) \n'       
print 'policy*(s) = '
print pii.T
print '\n moves : '
print m

print '\n directions : '
print d


# In[247]:

#policy iteration

def policyiteration(policy):
    
    newpolicy = np.zeros(ns,dtype=int)
    ppi = np.zeros((ns,ns))
    vps = np.zeros(ns)
    count = 0

    while 1:
        
        count +=1
        
        for s in xrange(ns):
            for sdash in xrange(ns):
                if policy[s] == 0:
                    for k in a1:
                        if ((k[0]==(s+1)) and (k[1]==(sdash+1))):
                            ppi[s][sdash] = k[2]
                            break
                if policy[s] == 1:
                    for k in a2:
                        if ((k[0]==(s+1)) and (k[1]==(sdash+1))):
                            ppi[s][sdash] = k[2]
                            break
                if policy[s] == 2:
                    for k in a3:
                        if ((k[0]==(s+1)) and (k[1]==(sdash+1))):
                            ppi[s][sdash] = k[2]
                            break
                if policy[s] == 3:
                    for k in a4:
                        if ((k[0]==(s+1)) and (k[1]==(sdash+1))):
                            ppi[s][sdash] = k[2]
                            break

        np.copyto(vpi, np.dot(np.linalg.pinv(np.eye(ns) - gamma*ppi), r))

        for s in xrange(ns):
            sum1=0.0
            sum2=0.0
            sum3=0.0
            sum4=0.0
            for row in range(int(a1.shape[0])):
                if (s == (int(a1[row][0])-1)):
                    sum1 += a1[row][2]*vpi[int(a1[row][1])-1]
                if (s == (int(a2[row][0])-1)):
                    sum2 += a2[row][2]*vpi[int(a2[row][1])-1]
                if (s == (int(a3[row][0])-1)):
                    sum3 += a3[row][2]*vpi[int(a3[row][1])-1]
                if (s == (int(a4[row][0])-1)):
                    sum4 += a4[row][2]*vpi[int(a4[row][1])-1]

            newpolicy[s] = np.argmax([sum1, sum2, sum3, sum4])

        if np.equal(policy,newpolicy).all():
            break
        else:
            np.copyto(policy,newpolicy)
            
    print 'no of iterations : ' + str(count)
    print '\n V*(s) = '
    print np.reshape(np.around(vpi,3), (9,9)).T
    return policy


# In[254]:

#RANDOM
print ' 7.2(c) \n'
print 'FOR RANDOM \n'
policy = np.random.randint(0,4,size=ns)
policy = policyiteration(policy)
print '\n policy*(s) = '
print policy.reshape((9,9)).T + 1
print '\n YES, it agrees with result from part (b) \n'
#EAST
print '\n (i) \n'
print 'FOR EAST \n'
policy = np.array([2]*ns)
policy = policyiteration(policy)
print '\n policy*(s) = '
print policy.reshape((9,9)).T + 1
#WEST
print '\n (ii) \n'
print 'FOR WEST \n'
policy = np.array([0]*ns)
policy = policyiteration(policy)
print '\n policy*(s) = '
print policy.reshape((9,9)).T + 1


# In[ ]:



