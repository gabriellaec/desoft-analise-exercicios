def calcula_total_da_nota(x, y):
    i=0
    total=0
    while i<len(preco) and i<len(quantidade):
        total=preco[i]*quantidade[i]
        i=i+1
        total=total+total
    return final
preco=[10]
quantidade=[3]
print(calcula_total_da_nota(preco,quantidade))