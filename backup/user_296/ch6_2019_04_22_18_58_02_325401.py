def encontra_maximo(a):
    i = 0 
    b = 0
    while i < len(a):
        if a[i] >= a[i-1]:
            b = a[i]
        i += 1 
    return b
lista = []
print(encontra_maximo(lista))
        
    