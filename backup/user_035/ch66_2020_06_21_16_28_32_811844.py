def lista_sufixos(palavra):
    if len(palavra) == 0:
        return []
    else:
        lista = [palavra]
        for i in range(len(palavra)):
            novo = palavra[i:]
            lista.append(novo)
        return lista