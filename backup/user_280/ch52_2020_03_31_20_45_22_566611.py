preços = []
quantidade = []
def calcula_total_da_nota(preços, quantidade):
    total=[]
    i=0
    while i<=len(preços):
        total[i] = preços[i]*quantidade[i]
        i += 1
    return total