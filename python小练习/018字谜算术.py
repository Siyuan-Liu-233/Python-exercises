import itertools as it
num=[i for i in range(10)]
for i in it.permutations(num,8):
	s,e,n,d,m,o,r,y=i
	if (s+m)*1000+(e+o)*100+(n+r)*10+(d+e)==m*10000+o*1000+n*100+e*10+y and m!=0:
		print('  %d%d%d%d\n+ %d%d%d%d\n-------\n=%d%d%d%d%d'%(s,e,n,d,m,o,r,e,m,o,n,e,y))

