import numpy as np
money=np.zeros((1,12))
for i in range(12):
    a=input()
    money[0,i]=float(a)
m=money.mean()
print('$%.2f'%m)
