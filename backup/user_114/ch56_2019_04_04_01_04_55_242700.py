def calcula_total_nota(x, y):
    i=0
    final=0
    while i<len(preco):
        total=preco[i]*quantidade[i]
        i=i+1
        final=final+total
    return final
preco=[10,15,20,30,40,50]
quantidade=[3,5,6,4,2,7]
print(calcula_total_nota(preco,quantidade))