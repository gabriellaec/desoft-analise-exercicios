def lista_caracteres(string):
    lista = []
   
    for i in string.lower():
        if i not in lista:
            lista.append(i)
            
    return lista
