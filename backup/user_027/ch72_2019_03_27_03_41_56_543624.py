def lista_caracteres(x):
    lista = []
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    for i in x:
        if i not in lista:
            lista.append(alfabeto[alfabeto.find(i)])        
    return lista