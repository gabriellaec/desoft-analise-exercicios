def esconde_senha(string):
    lista = []
    i=0
    while i<len(string):
        lista.append('*')
        i+=1
    j = 1
    while j < len(lista):
        frase += lista[j]
        j+=1
    return frase