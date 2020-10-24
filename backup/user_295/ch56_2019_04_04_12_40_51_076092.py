def calcula_total_da_nota (lista_preco, lista_quantidade):
    i = [0]
    while i < len(lista_preco):
        total = lista_preco [i] * lista_quantidade [i]
        i += 1
    return total