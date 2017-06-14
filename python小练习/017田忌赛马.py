# 这题也是华为面试时候的机试题：

# “ 广义田忌赛马：每匹马都有一个能力指数，齐威王先选马（按能力从大到小排列），田忌后选，马的能力大的一方获胜，若马的能力相同，也是齐威王胜（东道主优势）。”
# 例如：
# 齐威王的马的列表 a = [15,11,9,8,6,5,1]
# 田忌的马的候选表 b = [10,8,7,6,5,3,2]

# 如果你是田忌，如何在劣势很明显的情况下，扭转战局呢？
# 请用python写出解法，输出田忌的对阵列表 c及最终胜败的结果
# 评分

a = [8,15,1,11,6,5,9]
b = [2,8,6,7,5,3,10]

import numpy as np

a,b=np.array(np.sort(a)),np.array(np.sort(b))
x=np.shape(a)[0]
print(a,b)
time=0
print((a-b)>0)
while (((a-b)>0).sum())>=x/2 and time<x:
	temp=b[-1-time]
	b[0:-1-time],b[-1-time]=b[1:x-time],b[0]
	time+=1

if ((a-b)>0).sum()<x/2:
	print("获胜方案为：",a,b)
else:
	print('无法获胜')
