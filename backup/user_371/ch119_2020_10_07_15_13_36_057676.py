from math import factorial
def calcula_euler(x, n):
    lista=[]
    j=2
    while j<n:
        lista.append(j)
        j+=1
    i=0
    print(lista)
    lista_nova=[]
    e=1+x
    while i<len(lista):
        lista_nova.append((x**lista[i])/factorial(lista[i]))
        i+=1
        print(lista_nova)
    i=0
    while i<len(lista_nova):
        e=e+lista_nova[i]
        i+=1
    return e