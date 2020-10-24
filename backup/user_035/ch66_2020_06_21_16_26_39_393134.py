def lista_sufixos(palavra):
    if len(palavra) == 0:
        return []
    else:
        lista = [palavra]
        for i in range(len(palavra)):
            palavra = palavra[:i]
            lista.append(palavra)
        return lista