def acha_bigramas(palavra):
    lista_b = []
    for i in range(len(palavra)):
        lista_b.append(palavra[i]+palavra[i+1])
    return lista_b
        