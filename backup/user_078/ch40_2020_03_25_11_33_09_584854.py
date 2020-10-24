def soma_valores(s,i):
    s=0
    i=0
    while i<len(valores):
        s= s+valores[i]
        i=i+1
    return s 
lista=[5, 7 ,9 ,11]
resultado=soma_elementos(lista)
print (resultado)