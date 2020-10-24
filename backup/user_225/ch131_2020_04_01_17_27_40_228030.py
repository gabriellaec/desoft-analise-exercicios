import random
dado1 = random.randint(1,10)
dado2 = random.randint(1,10)
soma = dado1 + dado2
dinheiro = 10

print("Fase de Dicas")
n1 = int(input("Um número: "))
n2 = int(input("Um número maior ou igual ao anterior: "))
if soma < n1:
    print("Soma menor")
elif soma > n2:
    print("Soma maior")
else:
    print("Soma no meio")

print("Fase de Chutes")
print("Você tem {0} dinheiro(s)".format(dinheiro))
c = int(input("Quantos chutes você quer comprar? "))
dinheiro -= c
n3 = 0
while c > 0 and n3!=soma:
    n3 = int(input("Um número: "))
    c -= 1
if n3 == soma:
    dinheiro = dinheiro + (5 * dinheiro)
print("Você terminou o jogo com {0} dinheiros".format(dinheiro))