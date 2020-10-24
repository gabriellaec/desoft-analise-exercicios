contador = 0
soma = 0

while i <= 100:
    soma = soma + 1/(2 ** contador)
    contador += 1

print(soma)