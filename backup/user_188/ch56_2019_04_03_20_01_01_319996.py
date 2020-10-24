def calcula_total_da_nota(lista1, lista2):
    contador = 0
    valor_cada_item = []
    while contador < len(lista1):
        valor_cada_item.append(lista1[contador] * lista2[contador])
        contador += 1
    valor_total = sum(valor_cada_item)
    return valor_cada_item