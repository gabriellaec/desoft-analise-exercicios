def apaga_repetidos(frase):
    lista = []
    palavra = ''
    for i in frase:
        if not i in lista:
            lista.append(i)
            palavra += i
        else:
            palavra += '*'
    
    return palavra
