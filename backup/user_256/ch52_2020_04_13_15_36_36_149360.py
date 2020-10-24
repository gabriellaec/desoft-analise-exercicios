def  calcula_total_da_nota(preços, quantidade):
    vazia=[]
    i=0
    while i<len(preços):
        total = preços[i]*quantidade[i]
        vazia.append(total)
        i+=1
    return vazia