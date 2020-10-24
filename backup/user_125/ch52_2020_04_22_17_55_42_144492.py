def calcula_total_da_nota(listaprodutos,listaqtd):
    i=0
    soma=0
    zipped=zip(listaprodutos,listaqtd)
    for listaprodutos,listaqtd in zipped:
        multiplicacao= (listaprodutos)*(listaqtd)
        soma+=multiplicacao
        i+=1