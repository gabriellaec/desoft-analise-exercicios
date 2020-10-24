def calcula_total_da_nota(valor, qtd):
    valor=[]
    qtd=[]
    total=0
    i=0
    while i<len(valor) and i<len(qtd):
        f=valor[i]*qtd[i]
        total+=f
        i+=1
    return total