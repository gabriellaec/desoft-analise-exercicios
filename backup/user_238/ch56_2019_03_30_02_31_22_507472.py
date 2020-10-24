def calcula_total_da_nota(itens, preco):
    i=0
    soma=0
    while i < len(preco):
        soma+= itens[i]*preco[i]
        i+=1
    return soma
a=[2,3,1,1,4]
b=[1,2,3,4,5]
print(calcula_total_da_nota(a,b))
