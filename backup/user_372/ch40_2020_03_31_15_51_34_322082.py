def soma_valores(lista):
    num=len(lista)
    lista=[0]*num
    i=0
    soma=0
    while i<num:
        soma+=lista[i]
        i=i+1
print(soma_valores(5))