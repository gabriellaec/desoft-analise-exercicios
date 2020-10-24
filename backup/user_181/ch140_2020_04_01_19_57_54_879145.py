def faixa_notas(lista_inicial):
    inf_5 = lista_inicial.count(1,2,3,4)
    de_5_a_7 = lista_inicial.count(5,6,7)
    acima_7 = lista_inicial.count(8,9,10)
    lista_final = [inf_5 + de_5_a_7 + acima_7]
    return lista_final