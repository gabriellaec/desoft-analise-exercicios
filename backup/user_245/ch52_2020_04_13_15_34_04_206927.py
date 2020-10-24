def calcula_total_da_nota(precos,quantidade):
    cont = 0
    soma = 0
    while cont < len(precos):
        soma +=precos[cont]*quantidade[cont]
        cont+=1
    return soma
    