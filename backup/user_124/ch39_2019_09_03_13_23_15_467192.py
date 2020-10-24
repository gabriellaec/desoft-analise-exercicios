numero = int(input("digite um numero / 0 para parar :"))
soma = 0
while numero != 0:
    soma = soma + numero
    numero = int(input("digite um numero / 0 para parar :"))
    if numero == 0:
        print(soma)
        