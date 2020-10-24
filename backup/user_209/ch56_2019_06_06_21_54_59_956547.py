def calcula_total_da_nota (lista1,lista2):
    total = 0
    soma_quantidade = 0
    soma_preco = 0
    for quantidade in lista1:
        soma_quantidade += quantidade
        for preco in lista2:
            soma_preco += preco
    total = soma_quantidade * soma_preco
    return total