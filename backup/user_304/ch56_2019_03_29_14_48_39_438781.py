def calcula_total_da_nota (preco, produto):
    nota=[]
    i=0
    while i<len(preco):
        total=preco[i]*produto[i]
        nota.append (total)
        i+=1
    return nota
        
        
        