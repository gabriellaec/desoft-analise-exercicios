def calcula_total_da_nota(listaprodutos,listaqtd):
    i=0
    soma=0
    for listaprodutos in listaqtd:
        multiplicacao= listaprodutos[i]*listaqtd[i]
        soma+=multiplicacao
        i+=1
        print (soma)
    