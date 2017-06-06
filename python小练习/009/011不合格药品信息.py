from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen('http://forex.cngold.com.cn/gnrd/20161128d11024n102854893.html')
bsObj=BeautifulSoup(html)
a=bsObj.findAll('table',{'width':"580", 'border':"0",\
	'cellspacing':"1" ,'cellpadding':"5",'align':"center",'class':"cms_autoformat_table"})
print('不合格药品:')
for i in a[0].tr.next_siblings:
	b=i.find('td').text
	if b[-1] not in ['司','册'] and \
	not(b[-1].isdigit())and not(b[0].isdigit()):
		print(b)
