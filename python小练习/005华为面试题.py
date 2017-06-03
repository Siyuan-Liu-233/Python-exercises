#这题据说是华为公司的面试题，争取10分钟内完成。

# 假设有2个列表a和b，都是由任意整数构成，无序，例如a=[1,3,5,7,9], b=[2,4,6,8,10] (假设a与b长度相等，有能力可以做加分题：a与b长度不相等）

# 现在要求可以任意交换a与b中的项（使原始a列和b列长度不变），使新的列表a的和 与 新的列表b的和 之间的差距最小。
# 例如，新的a=[1,10,3,8,5], 新的b=[2,9,4,7,6]
#迭代法 效率较低
# import itertools
# import random as r
# a=[r.randint(1,100) for i in range(100)]
# b=[r.randint(1,100) for i in range(100)]
# c = a + b
# min1 = sum(c)
# for i in itertools.combinations(c, len(a)):
#     if abs(sum(i) - sum(c) / 2) < min1:
#         min1 = abs(sum(i) - sum(c) / 2)
#         a = i
# print('a = ', list(a))
# for i in list (a):c.remove(i)
# print('b = ',c)

###################################################
#动态规划解法
import random as r
a=[r.randint(1,100) for i in range(100)]
b=[r.randint(1,100) for i in range(100)]
a.sort()
b.sort()
newa=[a.pop()]
newb=[b.pop()]
while len(a)>0:
  c=a.pop()
  d=b.pop()
  if sum(newa)>sum(newb):
    newa.append(min(c,d))
    newb.append(max(c,d))
  else:
    newa.append(max(c,d))
    newb.append(min(c,d))
print (sum(newa),sum(newb))

