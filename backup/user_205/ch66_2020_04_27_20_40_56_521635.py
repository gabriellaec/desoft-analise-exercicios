def lista_sufixos(palavra):
    lista = []
    for i in range(len(palavra)):
        lista.append(palavra[i:])
    return lista
        
        