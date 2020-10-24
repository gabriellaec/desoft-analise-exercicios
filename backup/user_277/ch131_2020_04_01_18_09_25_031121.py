from random import randint
f=True
dado_1 = randint(1,10)
dado_2 = randint(1,10)
print(dado_1+dado_2)
dinheiro=10
numero_1 = int(input("Escolha um número:"))
numero_2 = int(input("Escolha um numero maior ou igual ao anterior:"))
soma=dado_1+dado_2
if soma<numero_1:
    print("Soma menor")
elif soma>numero_2:
    print("Soma maior")
else:
    print("Soma no meio")
print('seu dinheiro é {0}'.format(dinheiro))
aposta=int(input("Quanto você quer apostar:"))
dinheiro=dinheiro-aposta
while aposta>0 and f:
    k=int(input("Chute a soma dos dados:"))
    aposta-=1
    if k==soma:
        fim=5*(dinheiro-aposta)
        f=False
print("Você terminou o jogo com {0} dinheiros".format(fim)) 