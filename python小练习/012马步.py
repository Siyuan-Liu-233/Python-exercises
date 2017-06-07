# 周末我们就研究一下象棋中“马”的日字形走法吧。

# 我们知道“马”只能“日”字形行走（横向“日”字形也可）。

# 假设我有一个8x8的国际象棋棋盘，在棋盘的左下角（0,0）的位置有一个“马”，那么如果只走1步的话，这个“马”可能出现的位置是（1,2），（2,1）。

# 现在的问题是这个“马”应该怎么走才能到对角（7,7）呢？

# ==========
# |              1    1 |
# |                       |
# |           1    1    |
# |                       |
# |         1            |
# |                       |
# |       1              |
# | 1                    |
# ==========
# 输出结果像这样：
# Done!
# (0, 0)
# (2, 1)
# (3, 3)
# (4, 5)
# (5, 7)
# (6, 5)
# (7, 7)

import numpy as np
allPosition=np.zeros((8,8))
start=(0,0)
end=(7,7)
allPosition[end]=1
dxy=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
direction={}
p_now=end
p_next_list=[]
try_list=[]
while p_now!=start:
	for d in dxy:
		p_next=(p_now[0]+d[0],p_now[1]+d[1])
		if 0<=p_next[0]<8 and 0<=p_next[1]<8 and allPosition[p_next]!=1:
			allPosition[p_next]=1
			direction[p_next]=p_now
			try_list.append(p_next)
	try:
		p_now=try_list.pop(0)
	except:
		print('can not find')
		exit()
else:
	print('find!')
	p=start
	while p!=end:
		print(p)
		p=direction[p]
	print(p)




