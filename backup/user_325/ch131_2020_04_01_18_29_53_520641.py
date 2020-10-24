from random import randint
dado1 = randint(1,10)
dado2 = randint(1,10)
dinheiro = 10
jogada1 = int(input("Digite um numero:"))
jogada2 = int(input("Digite um numero maior ou igual ao anterior:"))
soma_dado = dado1 + dado2
if soma_dado < jogada1:
    print("Soma menor")
elif soma_dado > jogada2:
    print("Soma maior")
else:
    print("Soma no meio")
print(dinheiro)
compra_chute = int(input("Quantos chutes deseja comprar?:"))
dinheiro = dinheiro - compra_chute
while compra_chute!=0:
    tentativas = int(input("Digite um numero:"))
    if tentativas!= soma_dado:
        compra_chute -= 1
    else:
        dinheiro = dinheiro + (dinheiro*5)
        break
print("Você terminou o jogo com {0} dinheiros".format(dinheiro))