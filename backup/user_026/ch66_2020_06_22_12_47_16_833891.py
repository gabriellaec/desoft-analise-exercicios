def lista_sufixos(palavra):
    i = 0 
    lista = []
    while i <len(palavra):
        lista.append(palavra[i:])
        i+=1
    return lista