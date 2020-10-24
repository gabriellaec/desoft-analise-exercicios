def lista_sufixos(string):
    lista = []
    
    i = len(string);
    
    string2 = string[::-1]
    
    while i > 0:
        lista.append(string2[:i])
        i = i - 1
    
    return lista