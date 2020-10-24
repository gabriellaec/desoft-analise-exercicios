def soma_valores (lista):
    i=0
    soma=0
    while i<len(lista):
        soma+=lista[i]
        i+=1
    return soma 

v=[2,1,3]
resultado= soma_elementos(v)
print(resultado)
