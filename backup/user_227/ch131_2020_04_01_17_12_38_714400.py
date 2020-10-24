import random
#lançamento dos dados
dado1=random.randint(1,10)
dado2=random.randint(1,10)
soma=dado1+dado2
#valor de dinheiros
dinheiros=10
#fase de dicas
numero1=int(input("Digite um número: ")
numero2=int(input("Digite outro número maior ou igual ao anterior: ")
if soma<numero1:
    print("Soma menor")
elif soma>numero2:
    print("Soma maior")
else:
    print("Soma no meio")
#fase de chutes
print("Você tem {0} dinheiros disponível".format(dinheiros))
chutes=int(input("Quantos chutes quer comprar (cada chute custa 1 dinheiro)? ")
dinheiros-=chutes
condicao=True
while chutes>0 and condicao:
    chute=int(input("Chute um número: ")
    if chute==soma:
        dinheiros*=5
        condicao=False
    else:
        chutes-=1
#final do jogo
print("Você terminou o jogo com {0} dinheiros".format(dinheiros))      