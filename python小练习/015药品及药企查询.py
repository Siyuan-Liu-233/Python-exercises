# 接下来几个小练习，我会和大家分享如何利用python做一个“中国药品及药企查询系统”，并且编译成windows可以直接运行的exe文件，所涉及的内容包括requests库，医药查询系统的api，地图api接口，pyinstaller编译等。

# 第一篇：（py程序编写）
# 提示：
# 1. 利用百度API的药品查询（http://apis.baidu.com/medlive/drugs/drugapi），可以进行药品的查询
# 2. 利用百度API的药厂查询（http://apis.baidu.com/tngou/factory），可以进行药厂的查询
# 以上2个API都是开放端口，并且是免费的，只要申请个百度账号就可以使用。
# 3. 利用百度地图的静态API端口，可以转化经纬度坐标至百度地图（http://api.map.baidu.com/staticimage/v2）


import urllib.request
import json
apikey = '19ce61de2f7dde79fe2eca5511c3a940'
header = {'apikey': apikey}

print ('='*50)
print ('         欢迎进入中国药品及药企查询系统！')
print ('-'*50)
while True:
    print ('输入（1）药品名称 或者（2）药厂名称进行查找，输入（0）退出...')
    choose = input('>>>')
    if choose == '0':
        print ('感谢使用本系统！')
        input ()
        exit()
    elif choose == '1':
        print ('请输入你要查询的药品名称：')
        _drug = input('>>>')
        urldrug = 'http://apis.baidu.com/medlive/drugs/drugapi?type=list&key=%s&page=18pagesize=10' % _drug
        drugres = urllib.request.Request(urldrug,headers=header)
        drugres=urllib.request.urlopen(drugres)
        drugjs = json.loads(drugres.read())
        if drugjs.get('errNum',1000) != 0:
            print ('查询错误，请重新输入！')
            input ()
        else:
            drugdata = drugjs['retData']['data']
            for eachdrug in drugdata:
                print ('Id: ', eachdrug['drugId'], '  \t名称: ', eachdrug['dsName'])
            print ('输入你要查询的药品Id:')
            _drugid = input('>>>')
            urldrugid = 'http://apis.baidu.com/medlive/drugs/drugapi?type=show&drugid=%s' % _drugid
            drugidres = urllib.request.urlopen(urldrugid, headers=header)
            drugidjs = json.loads(drugidres.read())
            if drugidjs.get('errNum',1000) != 0:
                print ('查询错误，请重新输入！')
                input ()
            else:
                drugiddtdata = drugidjs['retData']['detail']
                for dt in drugiddtdata:
                    print (dt['ddf_name'],': ',dt['dd_value'])
                print ('感谢使用本系统！')
                input ()
    elif choose == '2':
        print ('请输入你要查询的药厂名称（全称）：')
        _name = input('>>>')
        urlname = 'http://apis.baidu.com/tngou/factory/name?name=%s' % _name
        nameres = rs.post(urlname, headers=header)
        namejs = json.loads(nameres.text)
        if namejs.get('status',False) == False:
            print ('查询错误，请重新输入！')
            input ()
        else:
            print ('药厂名称： ',namejs['name'])
            print ('药厂编号： ',namejs['number'])
            print ('药厂地址： ',namejs['paddress'])
            print ('药厂法人： ',namejs['legal'])
            print ('药厂电话： ',namejs['tel'])
            print ('药厂网址： ',namejs['url'])
            print ('药厂邮编： ',namejs['zipcode'])
            print ('药厂地图： ','http://api.map.baidu.com/staticimage/v2?ak=GVbSTEgzFooVjLVqfmzTrGRO1fGhWPVG&center=%s,%s&width=600&height=400&zoom=15&markers=%s,%s&markerStyles=l' % (namejs['x'],namejs['y'],namejs['x'],namejs['y']))
            print ('感谢使用本系统！')
            input ()
    else:
        print ('您输入的序号有误，请重新输入！')
        input ()