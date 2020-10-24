def fatorial(n):
    valor=0
    fat=1
    while valor<n:
        valor+=1
        fat=fat*valor
    return fat



def fatorial(n):
    fat=0
    for i in range(n):
        fat*=i
    return fat