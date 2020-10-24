def soma_impares(l):
    soma = 0
    for i in l:
        if i%2 != 0:
            soma += i
            return soma
            
    