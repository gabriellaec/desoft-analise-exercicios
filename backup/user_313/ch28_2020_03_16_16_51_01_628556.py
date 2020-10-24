contador = 0
soma = 0

while contador <= 99:
    x = 1/(2**contador)
    soma = soma + x
    contador = contador + 1
    if (contador == 100):
        print(soma)