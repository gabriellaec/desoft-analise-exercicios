def calcula_total_da_nota(listaprodutos,listaqtd):
    i=0
    for listaprodutos in listaqtd:
        preco_total= int(listaprodutos[i])*int(listaqtd[i])
        i+=1
        return preco_total