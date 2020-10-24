def monta_mala(lista_de_pesos):
    lista_itens_dentro_limite_peso = []
    peso_total = 0
    while peso_total < 23:
        if peso_total + lista_de_pesos[0] > 23:
            break 
        else:
            peso_total += lista_de_pesos[0]
            lista_itens_dentro_limite_peso.append(lista_de_pesos[0])
            del(lista_de_pesos[0])
    return lista_itens_dentro_limite_peso
