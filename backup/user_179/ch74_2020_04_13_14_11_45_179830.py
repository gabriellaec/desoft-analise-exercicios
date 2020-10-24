def conta_bigramas (palavra):
    i = 0
    lista = []
    dicionario = {}
    while i < (len(palavra)-1):
        bigrama = palavra[i] + palavra[i+1]
        lista.append(bigrama)
        if lista[i] in dicionario:
            values = lista.count(lista[i])
            dicionario[lista[i]] = values
        else:
            dicionario[lista[i]] = 1
        i = i + 1
    return dicionario

{'ba': 1, 'an': 3, 'na': 3, 'a ': 1, ' n': 1, 'ni': 1, 'ic': 1}