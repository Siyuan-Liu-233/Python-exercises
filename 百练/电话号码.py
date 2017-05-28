def transFunc(inNumber):  # 将记忆码转变为号码
    trans = list([['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'R', 'S'],
                  ['T', 'U', 'V'], ['W', 'X', 'Y']])  # 转换表
    get = ''  # 得到的号码

    aim1 = 0  # 标记某一位是否为字符
    for i in range(len(inNumber)):
        for k in range(8):  # 判断第i位是否为字母
            if inNumber[i] == '-':
                aim1 = 1
                break
            if inNumber[i] in trans[k]:
                get = get + str(k + 2)

                aim1 = 1
                break
        if aim1 == 0:
            get = get + inNumber[i]  # 如果第i位不是字母则为它本身
        aim1 = 0
    get = get[0:3] + '-' + get[3:]
    return get

if __name__ == '__main__':
    numget = {}
    rep = 0
    print(transFunc('-2-4-2'))

    n = input('输入号码个数：n\n')
    for i in range(int(n)):
        b = input('输入号码 %d:' % (i + 1))
        num = transFunc(b)
        numget[num] = numget.get(num, 0) + 1    #统计每个号码个数
    numget = sorted(numget.items(), key=lambda x: x[0])     #排序
    for i in range(len(numget)):
        if numget[i][1] > 1:
            print(numget[i][0], numget[i][1])
            rep = 1
    if rep == 0:
        print('No duplicates')
    # print(numget)
