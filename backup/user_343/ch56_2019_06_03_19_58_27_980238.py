preco=[20,30,10]
qtd=[2,3,4]
def calcula_total_da_nota(preco,qtd):
    total=[]
    i=0
    while i < len(preco):
        total[i]=preco[i]*qtd[i]
        i+=1
    return total 