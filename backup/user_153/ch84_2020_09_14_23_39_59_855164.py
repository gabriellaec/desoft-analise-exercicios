def inverte_dicionario(dic):
    inv_dic = {}
    for key, value in dic.items():
        inv_dic[value] = []
    for key, value in dic.items():
        inv_dic[value].append(key)
    return inv_dic

# dic = {'Ana': 19, 'Bruno': 18, 'Carlos':20, 'João': 19 }
# inv_dic = inverte_dicionario(dic)
# print(inv_dic)