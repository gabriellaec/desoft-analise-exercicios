def inverte_dicionario (dic):
    dicao = {}
    for nome, idade in dic.items():
        if nome not in dicao:
            dicao[idade] = []
        dicao[idade].append(nome)
    return dicao
