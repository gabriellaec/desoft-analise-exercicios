import random as r
dados = r.randint(2,20)
dinheiro = 10
c = 1
print('Fase de dicas')
p1 = int(input('Um numero '))
p2 = int(input('Um numero maior ou igual ao anterior' ))
if dados < p1:
    print("Soma menor")
elif dados > p2:
    print("Soma maior")
else:
    print("Soma no meio")

print("Fase dos chutes")
print(dinheiro)
chutes = int(input("Quantos chutes quer comprar? "))
dinheiro = dinheiro - chutes
while(c <= chutes):
    tentativa = int(input("Chute um número: ")
    if tentativa != dados:
        c += 1
    else:
        dinheiro += dinheiro * 5
        break
print("Você terminou o jogo com {0} dinheiros".format(dinheiro))