def calcula_fibonacci (n):
    lista = [1,1]*n
    i = 0
    while i < (n+1):
        lista[i+1] = lista[i] + lista[i-1]
        i+=1
    return lista
        
        
    