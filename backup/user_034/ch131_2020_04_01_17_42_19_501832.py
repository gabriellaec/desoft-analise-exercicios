import random
dado_1 = random.randint(1,10)
dado_2 = random.randint(1,10)
dinheiro = 10
a = int(input("Digite um numero:"))
b = int(input("Digite um numero maior ou igual ao anterior:"))
soma_dado = dado_1 + dado_2
if soma_dado < a:
    print("Soma menor")
elif soma_dado > b:
    print("Soma maior")
else:
    print("Soma no meio")
print(dinheiro)
c = int(input("Quantos chutes deseja comprar?:"))
dinheiro = dinheiro - c
i=0
while c!=0:
    tentativa_de_chute = int(input("Digite um numero:"))
    if tentativa_de_chute != soma_dado:
        c = c - 1
    else:
        dinheiro = dinheiro + (5*dinheiro)
else:
    print("Você terminou o jogo com {0} dinheiros".format(dinheiro))
    
