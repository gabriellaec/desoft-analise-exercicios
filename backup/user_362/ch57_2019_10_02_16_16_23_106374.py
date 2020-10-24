def soma_impares(lista):
    lista_impares=[]
    lista_pares=[]
    soma=0
    for i in lista:
        if i % 2 == 0:
            lista_pares.append(i)
        else:
            lista_impares.append(i)
    for i in lista_impares:
        soma=soma+i
    return soma
lista=[1,2,3,4,5]            
print(soma_impares(lista))      
