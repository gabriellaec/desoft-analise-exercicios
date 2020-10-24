def lista_sufixos(string):
    string2 = string[::-1]
    
    lista = []
    lista2 = []
    l = len(string2)
    for i in range(0, len(string2)):
        lista.append(string2[:l-i])
    
    
    for e in lista:
        lista2.append(e[::-1])
    
    return lista2
       