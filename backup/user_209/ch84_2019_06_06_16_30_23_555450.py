def inverte_dicionario (dic):
    dicao = {}
    for nome, idade in dic.items():
        if idade not in dicao:
            dicao[idade] = []
        dicao[idade].append(nome)
    return dicao
print (inverte_dicionario(dic))