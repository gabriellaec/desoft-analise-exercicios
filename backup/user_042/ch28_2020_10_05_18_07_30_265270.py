e = 1
acumulador = 0
while e < 100:
    a = 1/(2**e)
    acumulador = acumulador + a
    e+= 1
soma = 1 + acumulador
print (soma)