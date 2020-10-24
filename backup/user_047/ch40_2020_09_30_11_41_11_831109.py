def soma_valores(x):
    contador = 0
    s=0
    soma = 0
    while contador<len(x):
        s = x[contador]
        soma = s + soma
        contador+=1
    return soma
z = soma_valores([5,1,2,3,4])
print (z)