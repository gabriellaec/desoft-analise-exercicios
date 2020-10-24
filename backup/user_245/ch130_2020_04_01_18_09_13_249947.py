def monta_mala(lista_de_peso):
    while sum(lista_de_peso) > 23:
        del lista_de_peso[-1]
        print (lista_de_peso)
    if sum(lista_de_peso)<23:
        return lista_de_peso