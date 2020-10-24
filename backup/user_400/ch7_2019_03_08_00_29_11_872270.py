lista = []
def calcula_norma(a):
    i = 0
    o = 0
    a = 0
    while i<len(a):
        a[i]=a[i]**2
        lista.append(a[i])
        i += 1
    while o<len(lista):
    	a += lista[o]
    	o += 1
    return a**(1/2)
    

        