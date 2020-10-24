def calcula_total_da_nota(preco,quantidade):
    somafinal = 0 
    for p,q in zip(preco,quantidade):
        somafinal += p*q
    return somafinal

print(calcula_total_da_nota(preco,quantidade))
        