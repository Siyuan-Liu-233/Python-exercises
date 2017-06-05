
import urllib.request
import json
import re
import time
from bs4 import BeautifulSoup
print( '维基百科“11月18日”词条的编辑者都来自哪里？')
print( '='*40)
url='https://zh.wikipedia.org/w/index.php?title=11%E6%9C%8818%E6%97%A5&action=history'
res = urllib.request.urlopen(url)
res=BeautifulSoup(res)


iplist = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',res.text)
iplist = set(iplist)

print(iplist)
for ip in iplist:

        checkurl = "http://api.map.baidu.com/location/ip?ak=32f38c9491f2da9eb61106aaab1e9739&ip="+ip+"&coor=bd09ll"
        response=urllib.request.urlopen(checkurl)
        js = json.loads(response.read())
        print(ip)
        try:
                print( js['content']['address'])
        except:
                print( 'Not found!',js)

