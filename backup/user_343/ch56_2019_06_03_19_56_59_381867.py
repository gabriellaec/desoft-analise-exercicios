def calcula_total_da_nota():
    preco=[20,30,10]
    qtd=[2,3,4]
    total=[]
    i=0
    while i < len(preco):
        total.append(preco[i]*qtd[i])
        i+=1
    return total 