def conta_bigramas(string):
    dic = dict()
    for i in string:
        for x in string:
            if i+x in string:
                if i+x in dic:
                    dic[i+x] += 1
                else:
                    dic[i+x] = 1
    return dic

print(conta_bigramas("banana nanica"))