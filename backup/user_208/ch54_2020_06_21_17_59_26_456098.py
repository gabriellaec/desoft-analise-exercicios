def calcula_fibonacci (n):
    lista = []
    lista[0] = 1
    lista[1] = 1
    while i < (n+1):
        lista[i+1] = lista[i] + lista[i-1]
    return lista
        
        
    