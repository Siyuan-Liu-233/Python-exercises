def inputSentence():
    input_sentence = []
    sum_animal, num_sentence = input('输入动物总数和句子个数').split()
    sum_animal = int(sum_animal.strip())
    num_sentence = int(num_sentence.strip())
    for i in range(num_sentence):
        getSentence = input()
        getSentence = getSentence.strip()
        getSentence = getSentence.split()
        getSentence = [int(x) for x in getSentence]
        input_sentence.append(getSentence)
    return input_sentence,sum_animal,num_sentence
def countFalseSentence(input_sentence, sum_animal, num_sentence):
    true_num=0
    true_sentence = []
    juge=1
    for i in input_sentence:
        if max(i) > sum_animal:
            juge=0
        elif i[0] == 1 and (([2, i[1], i[2]] in true_sentence) or ([2, i[2], i[1]] in true_sentence)):
            juge=0
        elif i[0] == 2 and i[1] == i[2]:
            juge=0
        elif i[0] == 2 and ([2,i[2],i[1]] in true_sentence):
            juge=0
        elif i[0]==2:
            for x in range(1,sum_animal+1):
                if [2,x,i[1]] in true_sentence and [2,i[2],x] not in true_sentence:
                    true_sentence.append([2,i[2],x])
        if  juge:
            if i not in true_sentence:
                true_sentence.append(i)
            true_num=true_num+1 
        juge=1
    print(true_sentence)
    print(num_sentence-true_num)
def main():
    input_sentence,sum_animal,num_sentence=inputSentence()
    # input_sentence=[[1,101,1],[2,1,2],[2,2,3],[2,3,3],[1,1,3],[2,3,1],[1,5,5]]
    # sum_animal=100
    # num_sentence=7
    countFalseSentence(input_sentence,sum_animal,num_sentence)




if __name__ == '__main__':
    main()
