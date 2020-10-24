def lista_sufixos(string):
    lista = []
    
    string = string.replace(" ", "")
    
    i = len(string);
    
    while i > 0:
        lista.append(string[:i])
        i = i - 1
    
    return lista