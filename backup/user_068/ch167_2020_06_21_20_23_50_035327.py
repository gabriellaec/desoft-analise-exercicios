def bairro_mais_custoso(dicionario):
    valor = 0
    maior_custo = 0
    for bairro in dicionario.keys():
        lista = dicionario[bairro]
        for i in range(6, len(lista)):
            valor += lista[i]
        if valor > maior_custo:
            maior_custo = valor
            top = bairro
                           
    return bairro
