import re
import os
os.chdir("004") #004是存放TXT的文件夹
num=len([i for i in os.listdir()])
with open("1234567.txt") as file_now:
	file_now=file_now.read()
	for i in range(num-2): 
		print(file_now)
		file_next=re.findall(r"(\d{3,})",file_now)
		if 'devide by 2' not in file_now:
			with open(file_next[0]+'.txt') as file_next:
				file_next=file_next.read()
		else:
			with open(str(int(file_next[0])//2)+'.txt') as file_next:
				file_next=file_next.read()
		file_now=file_next
print(file_now)


