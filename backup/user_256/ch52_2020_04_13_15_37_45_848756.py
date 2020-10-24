def  calcula_total_da_nota(preços, quantidade):
    vazia=0
    i=0
    while i<len(preços):
        total = preços[i]*quantidade[i]
        vazia+=total
        i+=1
    return vazia