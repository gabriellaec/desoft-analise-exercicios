def inverte_dicionario (dic):
    dicao = {}
    for nome, idade in dic.items():
        if nome not in dicao:
            dicao[idade] = nome
            dicao.append(nome)
        else:
            dic[nome] = idade
    return dicao
