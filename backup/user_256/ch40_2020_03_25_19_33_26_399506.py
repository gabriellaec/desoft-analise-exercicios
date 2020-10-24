def soma_valores(value):
    s=0
    i=0
    while i < len(value):
        s += value[i]
        i += 1
    return s
v = [3, 2, 4, 1]
resultado = soma_valores(v)
print(resultado)
     