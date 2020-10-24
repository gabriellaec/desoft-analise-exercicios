def calcula_norma(lista):
    i=0
    a=0
    while i <len(lista):
        a+=lista[i]**2
        i+=1
    return a
lista=[1,2,3]
q=calcula_norma(lista)
print(q)