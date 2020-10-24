def lista_sufixos(string):
    lista = []
    
    if string == "":
        return lista
    
    i = len(string);
    
    while i > -1:
        lista.append(string[:i]
        i = i - 1
    return lista