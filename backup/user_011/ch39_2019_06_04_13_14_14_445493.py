soma = 0
numeros  = True
while numeros:
    numero = int(input('digite um numero: '))
    if numero != 0:
        soma = soma + numero
    else:
        numeros = False

print(soma)
              