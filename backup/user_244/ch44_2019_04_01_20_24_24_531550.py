def soma_valores(x):
    i = 0 
    soma = 0 
    
    while i < len(x):
        soma += x[i]
        i += 1
    return soma

x = [1,2,3,4,5]

print(soma_valores(x))