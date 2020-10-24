def calcula_total_da_nota(lista_precos,lista_quantidade):
    i = 0
    preco = []
    while i < len(lista_quantidade) : 
        preco.append(lista_precos[i]*lista_quantidade[i])
        i += 1
    soma = 0
    contador = 0
    while contador < len(preco):
        soma += preco[contador]
        contador += 1 
    return soma