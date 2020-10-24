def inverte_dicionario(dicionario):
    dic = {}
    for nome in dicionario:
        idade = dicionario[nome]
        if idade in dic:
            dic[idade].append(nome)
            print('if')

        else:
            dic[idade] = [nome]
            print('else')
    return dic