def lista_sufixos(string):
    lista = []
    for i in range(len(string)):
        lista.append(lista[i:len(string)])
    
    return lista