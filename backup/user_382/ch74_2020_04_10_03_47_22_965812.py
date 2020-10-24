def conta_bigramas(word):
    dic = {}
    for i in range(len(word)):
        if word[i:i+2] not in dic:
            dic[word[i:i+2]] = 1
        else:
            dic[word[i:i+2]] += 1
    return dic 
