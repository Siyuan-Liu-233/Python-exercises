def input_letter():
    dict_letter = []
    while 1:
        a = input('输入词典：')
        if a != '#':
            dict_letter.append(a)
        else:
            break
    test_letter = []
    while 1:
        a = input('输入单词：')
        if a != '#':
            test_letter.append(a)
        else:
            break
    return dict_letter, test_letter


def letter_simi(cur_lettr, dict_letter):
    simi = []
    for i in range(len(cur_lettr)):  # 将当前字符删一个字母看是否存在于字典中
        test1_letter = cur_lettr[:i] + cur_lettr[i + 1:]
        if test1_letter in dict_letter:
            simi.append(test1_letter)
    for i in range(len(dict_letter)):
        for j in range(len(dict_letter[i])):  # 将字典中的词删一个字母看是否与当前字符相同
            test2_letter = dict_letter[i][:j] + dict_letter[i][j + 1:]
            if test2_letter == cur_lettr:
                simi.append(dict_letter[i])
    for i in range(len(dict_letter)):  # 查找只有一位不同的字符
        if len(dict_letter[i]) != len(cur_lettr):
            continue
        else:
            diff = 0
            for j in range(len(cur_lettr)):
                if dict_letter[i][j] != cur_lettr[j]:
                    diff += 1
            if diff == 1:
                simi.append(dict_letter[i])

    return simi


def main():
    dict_letter, test_letter = input_letter()
    for i in test_letter:
        if i in dict_letter:
            print('%s is correct' % i)
        else:
            simi = letter_simi(i, dict_letter)
            print('%s:' % i, end='')
            for j in simi:
                print(j, end=' ')
            print()

if __name__ == '__main__':
    main()
