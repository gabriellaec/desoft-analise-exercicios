lista = [3,1,4,87]
def soma_valores(lista):
    soma = 0
    i = 0
    for i in range(len(lista)):
        soma = lista[i] + soma
    return soma      
x = soma_valores(lista)            
print(x) 