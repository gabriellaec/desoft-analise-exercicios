from random import randint
dinheiro = 10
jogada1 = randint(1, 10)
jogada2 = randint(1, 10)
valor = jogada1+jogada2 
dica1 = int(input("Digite um número: "))
dica2 = int(input("Digite um número maior do que o anterior: "))
valordica = dica1 + dica2
if valordica < valor:
    print("Soma menor")
elif valordica > valor:
    print("Soma maior")
else:
    print("Soma no meio")
print("Você tem {0}".format(dinheiro))
num_tentativas = int(input("Quantos chutes você deseja comprar? "))
dinheiro -= num_tentativas
while num_tentativas > 0:
    print("Você tem {0}, chutes.".format(num_tentativas))
    num_tentativas -= 1
    chute = int(input("Adivinhe a soma: "))
    if chute == valor:
        dinheiro *= 5
    print("Que pena, você errou :-(")
if num_tentativas == 0:
    print("Você terminou o jogo com {0} dinheiros".format(dinheiro))