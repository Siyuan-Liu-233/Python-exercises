def inputData():
    a=input()
    a.strip()
    m,n=[int(x) for x in a.split()]
    xian=[]
    for i in range(m):
        longth=input()
        xian.append(float(longth))
    xian.sort()
    return xian,n


a,n=inputData()
#a=[8.02,7.43,4.57,5.39]
#b=4.57
b=a[0]
while 1:
    c=0
    for i in a :
        c+=i//b
    if c==n or b<0.01:
        break
    else:
        b=b-0.01
b=round(b,2) #保留2位小数
print('%.2f'%b)