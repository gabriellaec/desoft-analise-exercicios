lista = [3,1,4,87]
def soma_valores(lista):
    soma = 0
    i = 0
    while i < len(lista):
        soma = lista[i] + soma
        i += 1
    return soma      
x = soma_valores(lista)            
print(x) 