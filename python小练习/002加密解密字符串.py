# ^ 按位异或  
# ord('A')->65
# chr(65)->A

#获得加密字符串和密匙
def get_key():
	string=input("输入明文：")
	key=input("输入密钥匙：")
	return string,key
#加密操作
def encode_str(string,key):
	l_key=len(key)
	l_string=len(string)
	mima=''
	for i in range(l_string):
		num=ord(key[i%l_key])^ord(string[i])
		mima=mima+str(num)
		if i<l_string-1:
			mima=mima+','
	print("密文为:",mima)
	return mima
#解密操作
def decode_str():
	mima=input("请输入密码（用“,”分隔）：")
	key=input("输入密钥匙：")
	mima=mima.strip().split(',')
	mima=[int(i) for i in mima]
	l_key=len(key)
	l_mima=len(mima)
	string=''
	for i in range(l_mima):
		string=string+chr(ord(key[i%l_key])^mima[i])
	print("明文为：",string)
if __name__ == '__main__':
	string,key=get_key()
	encode_str(string,key)
	decode_str()
