from numpy import  array as nparr
from math import ceil
def fn_np(a,b):
    dif = abs(sum(a)-sum(b))/2
    c = abs(nparr(a,ndmin=2).T - b)*1.0  
    print(c)  
    c = abs(c - dif)
    print(c)
    m,y = c.argmin(),c.shape[1]
    coo = (ceil(m/y)-1, m % y)
    a[coo[0]],b[coo[1]] = b[coo[1]],a[coo[0]]
    return a,b

a=[1,3,5,7,9]; b=[2,4,6,8,10]
print(fn_np(a,b))
