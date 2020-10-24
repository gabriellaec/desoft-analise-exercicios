def impar (x):
    if x % 2 != 0:
        return True

def soma_impares (l1):
    soma = 0
    for i in range (len(l1)):
        if impar(l1[i]) == True:
            soma += l1[i]
        else: 
            soma = soma
    return soma