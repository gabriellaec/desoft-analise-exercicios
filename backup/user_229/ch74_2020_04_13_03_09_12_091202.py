def conta_bigramas(string):
    dic = dict()
    for i and x in string:
        if i+x in string:
            if i+x in dic:
                dic[i+x] += 1
            else:
                dic[i+x] = 1
    return dic

print(conta_bigramas("banana nanica"))