a=input()
a=a.strip()
input_para=[float(x) for x in a.split()]
x,y,m,n,L=input_para
t=0
while x!=y:
    x=x+m
    y=y+n
    if x>L:
        x=x-L
    if y>L:
        y=y-L
    t+=1   
print(t)

