a = [1, 2, 3, 4]
def soma_valores(a):
    soma = 0
    i = 0
    while i < len(a):
        soma+=a[i]
        i+=1
    return soma
print (soma)