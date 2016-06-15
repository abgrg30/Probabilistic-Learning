# coding: utf-8
path = 'F:/UCSD/AI/1/'
f = open(path+'hw1_word_counts_05.txt', 'r')
l = f.readlines()

vocab = []
count = []

for i in xrange(len(l)):
    templ = l[i].split()
    vocab.append(templ[0])
    count.append(float(templ[1]))
    
s = sum(count)
pw = [i/s for i in count]


# In[2]:

import numpy as np
dic = {}

n = 10

for i in xrange(n):
    j = np.argmax(pw)
    print vocab[j],pw[j]
    dic[j] = pw[j]
    pw[j] = 0
    
for key in dic:
    #print dic[key]
    pw[key] = dic[key]

dic = {}
print '\n'

for i in xrange(n):
    j = np.argmin(pw)
    print vocab[j],pw[j]
    dic[j] = pw[j]
    pw[j] = 1
    
for key in dic:
    #print dic[key]
    pw[key] = dic[key]

dic = {}


# In[3]:

def check(ch, idx, word):
    if ch == word[idx] and ch not in word[:idx] and ch not in word[idx+1:]:
        return True
    
    return False

def func(present, absent): #present = list of tuples Eg [('U',1)], absent = list Eg ['A','E','I','O','S']
    l = []
    
    for i in xrange(len(vocab)):
        flag = 1
        for j in absent:
            if j in vocab[i]:
                flag = 0
                l.append(0)
                break
        
        if flag == 1:
            for j in present:
                if check(j[0], j[1], vocab[i]) == True:
                    continue
                else:
                    l.append(0)
                    flag = 0
                    break
            
            if flag == 1:
                l.append(1)
                    
    return l           

def func2(ch, present, absent):
    l = []
    temp = []
    
    for i in present:
        temp.append(i[1])
    
    for i in xrange(len(vocab)):        
        flag = 1
        
        for j in absent:
            if j in vocab[i]:
                l.append(0)
                flag = 0
                break
                
        if flag == 1:            
                
            for j in present:
                if check(j[0], j[1], vocab[i]) == True:
                    continue
                else:
                    l.append(0)
                    flag = 0
                    break
                    
            if flag == 1:
                if ch in vocab[i] and i not in temp:
                    l.append(1)
                else:
                    l.append(0)        

    return l

def calc(li, present, absent):
    pew = func(present, absent)
    plw = func2(li, present, absent)

    tpwe = sum([pew[i]*pw[i] for i in xrange(len(vocab))])

    pwe = [pew[i]*pw[i]/tpwe for i in xrange(len(vocab))]

    ple = sum([plw[i]*pwe[i] for i in xrange(len(vocab))])
    
    return ple


# In[4]:

import string

def func3(present, absent):
    maxi = 0
    new = 0
    temp = []

    for i in present:
        temp.append(i[0])

    for i in list(string.ascii_uppercase):    
        if i not in temp:
            new = calc(i, present, absent)

            if new > maxi:
                maxi = new
                li = i
    return li


# In[5]:

present = [('U',1)]
absent = ['A','E','I','O','S']
li = 'Y'
print li
print calc(li, present, absent)


# In[6]:

present = [('D',0),('I',3)]
absent = ['A']
li = 'E'
print li
print calc(li, present, absent)


# In[7]:

present = [('D',0),('I',3)]
absent = []
li = 'A'
print li
print calc(li, present, absent)


# In[8]:

present = []
absent = ['E','O']
li = 'I'
print li
print calc(li, present, absent)


# In[9]:

present = [('O',2)]
absent = ['A','E','M','N','T']
li = func3(present,absent)
print li
print calc(li, present, absent)


# In[10]:

present = [('A',0), ('S',4)]
absent = ['I']
li = func3(present,absent)
print li
print calc(li, present, absent)


# In[11]:

present = [('A',0), ('S',4)]
absent = []
li = func3(present,absent)
print li
print calc(li, present, absent)


# In[48]:

present = []
absent = ['E','A']
li = func3(present,absent)
print li
print calc(li, present, absent)


# In[49]:

present = []
absent = []
li = func3(present,absent)
print li
print calc(li, present, absent)

