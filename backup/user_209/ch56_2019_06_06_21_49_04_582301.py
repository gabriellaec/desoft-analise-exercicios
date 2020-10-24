def calcula_total_da_nota (lista1,lista2):
    total = 0
    for quantidade in lista1:
        for preco in lista2:
            total = quantidade*preco
    return total