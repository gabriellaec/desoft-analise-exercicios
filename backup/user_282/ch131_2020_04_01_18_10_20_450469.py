import random

dinheiros = 10
chutes = 0 
if dinheiros > 0:
    print('Você possui {0} dinheiros'.format(dinheiros))
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
    while chutes > 0:
        numero = int(input('Digite seu chute: ')) 
        if soma == numero:
            dinheiros *= 6
            break
        elif soma != numero:
            chutes -= 1
        
        
print("Você terminou o jogo com {0} dinheiros".format(dinheiros))

