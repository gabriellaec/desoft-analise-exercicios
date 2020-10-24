def lista_sufixos (string):
    i =0
    lista = []
    while i< len (string):
        lista.append (string[i:])
    return lista
