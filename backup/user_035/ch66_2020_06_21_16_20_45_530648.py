def lista_sufixos(palavra):
    if len(palavra) == 0:
        return []
    else:
        lista = [palavra]
        for i in range(len(palavra)):
            lista.append(palvara-palavra[i])
        return lista