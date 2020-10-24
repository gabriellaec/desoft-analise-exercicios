def simplifica_dict(dicionario):
    saida=[]
    for i in dicionario.keys():
        if i not in saida:
            saida.append(i)
    for j in dicionario.values():
        if j not in saida:
            saida.append(j)
    return saida