def conta_letras(word):
    dic = {}
    for i in word:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    return dic 
