def lista_sufixos(string):
    lista = []
    c = 0
    while c < len(string):    
        b = string[::(len(string)+c)]
        lista.append(b)
        c += 1
    return lista
    