lista_termos = []
def seq(n):
    if n < 1000:
        termos = 0
        if n % 2 == 0:
            eq = n/2
            termos += 1
        else:
            eq = 3*n + 1
            termos += 1
    lista_termos.append(termos)
            
            