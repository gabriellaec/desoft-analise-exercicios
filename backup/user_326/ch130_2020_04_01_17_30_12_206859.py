def monta_mala(lista_de_pesos):
    lista_itens_dentro_limite_peso = []
    peso_total = 0
    indice = 0
    while len(lista_de_pesos) > indice:
        if peso_total + lista_de_pesos[indice] > 23:
            break 
        else:
            peso_total += lista_de_pesos[indice]
            lista_itens_dentro_limite_peso.append(lista_de_pesos[indice])
            indice += 1
    return lista_itens_dentro_limite_peso