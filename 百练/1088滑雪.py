import numpy as np

    
def get_a():        #输入
    m=input()
    m,n=m.split()
    m=int(m)
    n=int(n)
    a=[]
    for i in range(m):
        line=input()
        line=line.strip()
        line=line.split()
        a.append(line)
    a=np.array(a,dtype='int64')
    return a 

def in_bound(x1,y1):        #判断是否出界
    return (0<=x1<(np.shape(a)[0]) and 0<=y1<(np.shape(a)[1]))

def get_step(x,y):
    if(b[x,y]!=1):      #b[x,y]已经计算过 直接返回
        return b[x,y]
    for i in range(4):
        # print(i)
        # print(in_bound(dx[i]+x,dy[i]+y))
        if (in_bound(dx[i]+x,dy[i]+y)==True):   #如果越界
            #print(dx[i]+x,dy[i]+y)
            if(a[dx[i]+x,dy[i]+y]<a[x,y]):  #周围存在可以向下滑的方向
                temp=get_step(dx[i]+x,dy[i]+y)+1;   #此时的步数值为其+1
                b[x,y]=temp if (temp>b[x,y]) else b[x,y] #得到最大的步数值
    return b[x,y]   #必须返回 因为上方运用了迭代
if __name__ == '__main__':
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    #a=np.array([[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]])
         
    #print(np.shape(a)[1])
    a=get_a()
    b=np.ones(np.shape(a))      #用来储存每个位置的最大步数
    for x in range(np.shape(a)[0]):
        for y in range(np.shape(a)[1]):
            #print(x,y)
            b[x,y]=get_step(x,y)
    print(np.max(b))
    
