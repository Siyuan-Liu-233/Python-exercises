
def getstr(m):
    strget=[]
    for i in range(m):
        strnow=input()
        strget.append(strnow)
    return strget           #输入



def number_re(inX,n):
    num=0
    for i in range(n-1):
        for j in range(i+1,n):
            if inX[i]>inX[j]:
                num+=1          #统计逆序对
    return num

def output(inX,m):         # 输显示
    for i in range(m):
        print(inX[i][0])


if __name__ == '__main__':
    getnum=input()
    n,m=getnum.split(' ')
    n,m=int(n),int(m)
    strget=getstr(m)
    sort_str={}
    for i in range(m):
        numnow=number_re(strget[i],n)
        sort_str[strget[i]]=numnow
    sort_str=sorted(sort_str.items(),key=lambda x:x[1]) #排序
    print('')
    output(sort_str,m)
    #print(sort_str)