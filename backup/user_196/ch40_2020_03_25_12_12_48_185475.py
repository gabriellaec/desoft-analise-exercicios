def soma_valores(k):
    soma = 0
    i = 0
    while i < len(k):
        soma+=a[i]
        i+=1
    return soma

a = [1, 2, 3, 4]
resultado = soma_valores(a)
print (resultado)