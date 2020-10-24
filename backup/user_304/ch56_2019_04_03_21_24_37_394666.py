def calcula_total_da_nota (preco, produto):
    i=0
    total=0
    while i<len(preco):
        nota=preco[i]*produto[i]
        total+=nota     
        i+=1
    return total
        
        
        