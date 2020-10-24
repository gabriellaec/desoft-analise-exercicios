import random
dado_1 = random.randint(1,10)
dado_2 = random.randint(1,10)
soma = dado_1 + dado_2

dinheiro = 10

p1 = int(input("Digite um numero: "))
p2 = int(input("Digite um numero maior: "))

if soma < p1:
    print("Soma menor")
elif soma > p2:
    print("Soma maior")
else:
    print("Soma no meio")

while dinheiro > 0:
    chutes = int(input("Quantos chutes quer comprar: "))
    dinheiro =  dinheiro - chutes
    i = 0
    while i <= chutes:
        player = int(input("Chute um numero: "))
        if player == soma:
            dinheiro = dinheiro + dinheiro*5
            break
        i += 1
    break
print("Você terminou o jogo com {0} dinheiros".format(dinheiro))