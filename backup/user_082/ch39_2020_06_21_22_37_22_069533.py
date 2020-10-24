def sequencia(numero):
    termos = [numero]
    while numero > 1:
        if numero % 2 == 0:
            termos.append(numero / 2)
    else:
        termos.append(3*numero+1)
    return termos

x = 0
y = 1
z = 0

while x < 1000:
    if len(sequencia(x)) > y:
        y = len(sequencia(x))
        z = x
    x += 1
print (z)
