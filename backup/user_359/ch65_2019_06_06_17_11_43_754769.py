def acha_bigramas(palavra):
    lista_b = []
    i = 1
    while i != len(palavra):
        if palavra[i-1] + palavra[i] not in lista_b:
        	lista_b.append(palavra[i-1] + palavra[i])
    return lista_b
        