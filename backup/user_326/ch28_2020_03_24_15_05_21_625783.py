n = 0
turnos = 0
while turnos < 100:
    valor = 1 / 2**n
    turnos += 1
    n += 1
    if n == 99:
        soma = n * (1 + valor) / 2
        print(soma)