# 前2个小练习大家学习了字典树的基本原理及应用。python小练习（008）：传送门

# 今天我淘气的侄子又把我的文件用zip压缩了，并用了3个小写字母组成的单词进行了加密，你能帮我破解这个zip文件吗？

#   readme.zip (195 Bytes, 下载次数: 19) 

# 提示：

# python自带的zipfile库：
# ZipFile.extract(member, path=None, pwd=None) 
# Extract a member from the archive to the current working directory; member must be its full name or a ZipInfo object). Its file information is extracted as accurately as possible. path specifies a different directory to extract to. member can be a filename or a ZipInfo object. pwd is the password used for encrypted files.

# Returns the normalized path created (a directory or new file).
#预备知识

#file=zipfile.ZipFile("文件", "r") 读取文件

#file.namelist()返回压缩文件夹中文件名字构成的列表

#file.extract(member, path=None, pwd=None)  member指的是压缩文件夹中要解压的文件名
#path是文件解压后的位置默认是当前路径，pwd是密码

#file.extractall(self, path=None, members=None, pwd=None)
#解压文件夹内所有文件 存放在path下 可赋值members解压部分文件


import zipfile

with zipfile.ZipFile("009\\readme.zip", "r") as myzip:
    print(myzip.namelist())
    for letter_0 in range(97, 123):
        for letter_1 in range(97, 123):
            for letter_2 in range(97, 123):
            	#解压的pwd必须是byte格式！！！
                pwd = bytes(chr(letter_0) + chr(letter_1) + chr(letter_2),encoding='utf-8')

                try:
                	#解压文件夹内所有文件 存放在path下 可赋值members解压部分文件
                    myzip.extractall(path='.\\009\\readme', pwd=pwd)
                    print("pwd={0}".format(pwd))
                    input()
                    exit()
                except:
                    continue
