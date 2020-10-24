def inverte_dicionario(dic):
    listanomes=[]
    for chave, valor in dic.items():
        dic[valor]= chave
        for chave2, valor2 in (dic.items()):
            if valor2==chave:
                listanomes.append(valor2)
        