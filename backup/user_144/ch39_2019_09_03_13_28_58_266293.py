numero = int(input("Digite um numero e ZERO  para parar"))

soma = 0
while numero != 0:
    soma = soma + numero
    numero = int(input("Digite um numero e ZERO  para parar"))
    if numero == 0:
        print(soma)