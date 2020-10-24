def inverte_dicionario(dic):
    idade= set(dic.values())
    dic1= {}
    for i in idade:
        dic1[i]=[j for j in dic.keys() if dic[j]==i]
    return dic1
dic={'Ana': 19, 'Bruno': 18, 'João': 19}
q=inverte_dicionario(dic)
print(q)