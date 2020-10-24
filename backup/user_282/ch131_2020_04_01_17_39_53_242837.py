import random

dinheiros = 10
chutes = 0 
while dinheiros > 0:
    dado1 = random.randint(1, 10)
    dado2 = random.randint(1, 10)
    soma = dado1 + dado2
    numero1 = int(input('Digite um numero: '))
    numero2 = int(input('Digite outro numero MAIOR ou IGUAL ao anterior: '))
    if soma < numero1:
        print("Soma menor")
    elif soma > numero2:
        print("Soma maior")
    else:
        print("Soma no meio")
    chutes = int(input('Quantos chutes você quer comprar? '))
    dinheiros -= chutes
    numero = int(input('Digite seu chute: '))    
    while chutes > 0:
        if soma == numero:
            dinheiros *= 5
        chutes -= 1
else:
    print("Você terminou o jogo com {0} dinheiros".format(dinheiros))