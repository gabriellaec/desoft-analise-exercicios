def apaga_repetidos(palavra):
    lista = []
    lista_final = []
    for i in palavra:
        if i.upper() in lista:
            lista_final.append('*')
        else:
            lista_final.append(i)        
        if i not in lista:
            lista.append(i.upper())
    a = ''.join(lista_final)
    return a.strip(',')