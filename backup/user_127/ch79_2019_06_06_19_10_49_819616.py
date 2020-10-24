def monta_dicionario(lis1, lis2):
    dic = {}
    for a in range(len(lis1)):
        dic[lis1[a]] = lis2[a]
    return dic
lisa = ['a', 'b', 'c']
lisb = ['d', 'e', 'f']
print(monta_dicionario(lisa, lisb))