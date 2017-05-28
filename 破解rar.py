import os
f=open('dic.txt') #打开测试密码文件
s=f.readlines()
f.close()
for p in s:
    cmd = "winrar e new.rar -y -p%s" % (p) #e表示解压缩 -y表示回应全为是 -p表示密码设置
    r = os.system(cmd)
    if r == 0:
        print("pass = %s" % p)
        break
input()        #这句可以不用写，我是为了双击打开时，最后破解完毕不会直接关闭窗口。
