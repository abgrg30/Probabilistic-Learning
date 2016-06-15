
# coding: utf-8

# In[13]:

import math
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# In[14]:

def f(x):
    return math.log(math.cosh(x))

def Q(x,y):
    return f(y) + (math.tanh(y))*(x-y) + 0.5*((x-y)**2)


# In[15]:

lfx = []
for i in xrange(-10,11):
    lfx.append(f(i))
plt.plot(range(-10,11),lfx, color='r', label='f(x)')

lQx2 = []
for i in xrange(-10,11):
    lQx2.append(Q(i,2))
plt.plot(range(-10,11),lQx2, color='g', label='Q(x,2)')

lQx3 = []
for i in xrange(-10,11):
    lQx3.append(Q(i,-3))
plt.plot(range(-10,11),lQx3, color='b', label='Q(x,-3)')
plt.legend()
plt.show()


# In[16]:

def auxiliary(xn):
    l = []
    l.append(xn)
    old = xn
    new = 0
    while abs(new-old)>0.0001:
        new = xn - math.tanh(xn)
        old = xn
        xn = new
        l.append(xn)
    return l

def newton(xn):
    l = []
    l.append(xn)
    old = xn
    new = 0
    while abs(new-old)>0.0001:
        new = xn - math.tanh(xn)*(math.cosh(xn)**2)
        print new
        old = xn
        xn = new
        l.append(xn)
    return l


# In[17]:

l2 = auxiliary(2)
l3 = auxiliary(-3)
print l2
print l3
plt.plot(range(len(l2)), l2, color='r', label='x0 = 2')
#plt.show()
plt.plot(range(len(l3)), l3, color='b', label='x0 = -3')
plt.legend()
plt.show()


# In[18]:

l2 = newton(2)


# In[19]:

l3 = newton(-3)


# In[20]:

def gx(k,x):
    sumi = 0
    for i in range(k):
        sumi += math.log(math.cosh(x + 1.0/math.sqrt(((i+1)**2)+1)))
    return (1.0/k)*sumi

l = []
for i in xrange(-5,6):
    l.append(gx(10,i))
plt.plot(range(-5,6), l, 'r')
plt.show()


# In[21]:

#No, it is not simple to find the exact minimum


# In[22]:

def update(xn):
    l = []
    l.append(xn)
    prev = xn
    new = 0
    while abs(new - prev) > 0.00001:
        sumi = 0
        for i in range(10):
            sumi += (math.tanh(xn + 1.0/math.sqrt(((i+1)**2)+1)))
        sumi=(1.0/10)*sumi
        new = xn - sumi
        prev = xn
        xn = new
        l.append(new)
    return l

l = update(2)
print l
plt.plot(range(len(l)), l, 'r')
plt.show()


# In[23]:

gx(10,-0.2521)


# In[ ]:



