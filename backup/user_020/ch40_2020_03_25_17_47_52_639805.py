def soma_numeros(valores):
    s = 0
    i = 0
    while i < len(valores):
        s += valores[i]
        i += 1
    return s

v=[3,2,4,1]
resultado = soma_numeros(v)
print(resultado)