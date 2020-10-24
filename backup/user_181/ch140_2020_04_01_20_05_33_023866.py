def faixa_notas(lista_inicial):
    arredonda = [round(num) for num in lista_inicial]
    um = lista_inicial.count(1)
    dois = lista_inicial.count(2)
    tres = lista_inicial.count(3)
    quatro = lista_inicial.count(4)
    inf_5 = um + dois + tres + quatro
    cinco = lista_inicial.count(5)
    seis = lista_inicial.count(6)
    sete = lista_inicial.count(7)
    de_5_a_7 = cinco + seis + sete
    oito = lista_inicial.count(8)
    nove = lista_inicial.count(9)
    dez = lista_inicial.count(10)
    acima_7 = oito + nove + dez
    lista_final = [inf_5, de_5_a_7, acima_7]
    return lista_final