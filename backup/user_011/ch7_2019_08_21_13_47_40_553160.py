def calcula_norma(lista):
    i = 0
    n = 0 
    while i < len(lista):
        n = lista[i]**2 + n
        i+=1
    return n**0.5
        
        