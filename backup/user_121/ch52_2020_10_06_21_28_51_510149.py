def calcula_total_da_nota(preco, quantidade):
    resultado=0
    i=0
    while i<len(preco) or i<len(quantidade):
        resultado+=preco[i]*quantidade[i]
        i+=1
    return resultado