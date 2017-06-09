maze=[[1,0,1,0,0,1],
	  [1,1,1,0,1,1],
	  [0,0,1,1,0,1],
	  [1,0,1,0,1,1],
	  [1,1,1,1,0,1],
	  [0,1,0,1,1,1]]
import numpy as np
maze=np.array(maze)

go_in=(0,0)
go_out=(5,5)
position_now=go_out
step=[(1,0),(-1,0),(0,1),(0,-1)]
visit=[]
rount={}
while position_now!=go_in:
	for (x,y) in step:
		position_before=(position_now[0]+x,position_now[1]+y)
		if 0<=position_before[0]<6 and 0<=position_before[1]<6 \
		and position_before not in rount and maze[position_before]==1:
			rount[position_before]=position_now
			visit.append(position_before)
	try:
		position_now=visit.pop(0)
	except:
		print("can't find")
		break
else:
	p=go_in
	print(p)
	while p!=go_out:
		p=rount[p]
		print(p)

	





