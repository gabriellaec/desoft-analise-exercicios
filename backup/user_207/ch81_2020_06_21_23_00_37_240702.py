def interseccao_valors(dicio1, dicio2):
    lista_valores = []
    for value in dicio1.value():
        if value in dicio2.value():
            lista_valores.append(value)
            
    return lista_valores