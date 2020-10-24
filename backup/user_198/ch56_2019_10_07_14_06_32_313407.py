def calcula_total_da_nota(preços,qtde):
    i=len(preços)
    total=0
    ind=0
    while ind<i:
        total+=(preços[ind])*(qtde[ind])
        ind+=1
    return total