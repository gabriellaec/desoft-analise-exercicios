def lista_caracteres(string):
    string = ''
    lista = []
    i = 0
    while i < len(string):
        if string[i+1] != string[i]:
            lista.append(string)
        i += 1
    return lista
        
        