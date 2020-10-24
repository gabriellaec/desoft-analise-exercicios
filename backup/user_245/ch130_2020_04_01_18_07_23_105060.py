def monta_mala(lista_de_peso):
    while sum(lista_de_peso) > 25:
        del lista_de_peso[-1]
        print (lista_de_peso)
    if sum(lista_de_peso)<25:
        return lista_de_peso