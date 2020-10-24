def soma_valores(valores):
    s = 0
    i = 0
    for i in range(i, len(valores)):
        s += valores[i]
        i += 1
    return s

v=[3,2,4,1]
resultado = soma_valores(v)
print(resultado)