from random import randint
dinheiro = 10
jogada1 = randint(1, 10)
jogada2 = randint(1, 10)
a = int(input("Digite um número: "))
b = int(input("Digite um número maior do que o anterior: "))
valordica = a + b
if valordica < a:
    print("Soma menor")
elif valordica > b:
    print("Soma maior")
else:
    print("Soma no meio")
print("Você tem {0}".format(dinheiro))
num_tentativas = int(input("Quantos chutes você deseja comprar? "))
dinheiro -= num_tentativas
while num_tentativas != 0:
    print("Você tem {0}, chutes.".format(num_tentativas))
    chute = int(input("Digite um valor pro seu chute: "))
    if chute != valordica
        num_tentativas -= 1
    else:
        dinheiro = dinheiro +(dinheiro*5)
        break
    print("Você terminou o jogo com {0} dinheiros".format(dinheiro))