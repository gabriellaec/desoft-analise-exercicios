def interseccao_valores(dicio1, dicio2):
    lista_valores = []
    for value in dicio1.values():
        if value in dicio2.values():
            lista_valores.append(value)
            
    return lista_valores