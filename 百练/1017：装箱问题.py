import numpy as np
import math
def input_simply():
    simply = []
    while 1:
        a = input()
        if a.strip() != '0 0 0 0 0 0':
            a = a.split()
            simply.append(a)
        else:
            break
    return simply

def output(simply):
    simply=np.int64(np.array(simply))
    m,n=np.shape(simply)
    for i in range(m):
        v=0
        for j in range(n):
            v+=simply[i,j]*(j+1)**2     #计算体积
        num=math.ceil(v/36) #向上取整   
        print(num)
if __name__ == '__main__':
    simply=input_simply()
    output(simply)