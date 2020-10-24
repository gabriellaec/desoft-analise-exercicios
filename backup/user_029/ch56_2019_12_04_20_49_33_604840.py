

def calcula_total_da_nota(preco,quantidade):
    somafinal = 0 
    for i in range(len(preco)):
        somafinal += preco[i]*quantidade[i]
    return somafinal
