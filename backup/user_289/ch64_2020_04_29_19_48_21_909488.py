def acha_bigramas(string):
    palavra = str(string)
    lista = []
    i = 0
    while i < len(palavra):
        for elemento in range(i,len(palavra)+1):
            bigrama = palavra[i] + elemento
            lista.append(bigrama)
    return lista