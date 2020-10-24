def calcula_total_da_nota(produtos,itens):
    i=0
    listatotal=[]
    total=0
    a=0
    while i<len(produtos):
        listatotal.append(produto[i]*itens[i])
        i+=1
        while a<len(listatotal):
            total+=listatotal[a]
            a+=1
    return total