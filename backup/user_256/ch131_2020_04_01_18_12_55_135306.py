#Fase1:
import random
dado1= random.randint(1, 10)
dado2= random.randint(1, 10)
sorteio = dado1+dado2
print("Voce tem 10 dinheiros")
dinheiro = 10
#Fase de dicas

nmr1 = int(input("Digite um numero: "))
if sorteio < nmr1:
    print("Soma menor")
nmr2 = int(input("Digite outro numero: "))
if sorteio > nmr2:
    print("Soma maior")
if not sorteio>nmr2 and not sorteio<nmr1:
    print("Soma no meio")
    
#Fase de chutes
nossa = True
while dinheiro>0 and nossa:
    print("Voce tem {}dinheiros".format(dinheiro))
    compra = int(input("Quantos chutes deseja comprar? "))
    dinheiro= dinheiro - compra
    while compra>0:
        chute=int(input("Qual a soma? "))
        compra = compra-1
        if chute == sorteio:
            dinheiro = dinheiro + dinheiro*5
            nossa = False
print("Você terminou o jogo com {0} dinheiros".format(dinheiro))