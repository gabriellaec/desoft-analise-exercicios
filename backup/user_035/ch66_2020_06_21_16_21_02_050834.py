def lista_sufixos(palavra):
    if len(palavra) == 0:
        return []
    else:
        lista = [palavra]
        for i in range(len(palavra)):
            lista.append(palavra-palavra[i])
        return lista