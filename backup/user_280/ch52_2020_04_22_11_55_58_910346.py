def calcula_total_da_nota(preços, quantidade):
    total=[]
    if preços == []:
        total = 0
    else:
        i=0
        while i<len(preços):
            total.append(preços[i]*quantidade[i])
            i += 1
    return total