def calcula_total_da_nota(preco,quantidade):
    contador=0
    soma=0
    while contador < len(preco):
        total=preco[contador]*quantidade[contador]
        contador+=1
        soma=soma+total
    return soma