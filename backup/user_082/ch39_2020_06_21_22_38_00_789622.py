def sequencia(numero):
    termos = [numero]
    while numero > 1:
        if numero % 2 == 0:
            numero = numero /2
            termos.append(numero)
    else:
        numero = 3 * numero + 1
        termos.append(numero)
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
