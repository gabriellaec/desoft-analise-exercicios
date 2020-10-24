preços = []
quantidade = []
i=0
def calcula_total_da_nota(preços, quantidade):
    total=[]
    while i<len(preços):
        total[i] = preços[i]*quantidade[i]
        i += 1
    return total
        
    