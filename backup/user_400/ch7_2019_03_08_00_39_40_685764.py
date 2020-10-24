lista = []
def calcula_norma(a):
    i = 0
    o = 0
    x = 0
    while i<len(a):
        a[i]=a[i]**2
        lista.append(a[i])
        i += 1
    while o<len(lista):
    	x += lista[o]
    	o += 1
    return round(x**(1/2), 2)
    

        