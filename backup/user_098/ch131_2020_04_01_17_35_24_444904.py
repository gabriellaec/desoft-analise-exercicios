from random import randint

Dado1 = randint(1, 10)
Dado2 = randint(1, 10)
SomaDados = Dado1+Dado2
print(SomaDados)
Dinheiro=10
Chutes=0

fase_inicial_n1 = int(input("Escolha um número:"))
fase_inicial_n2 = int(input("Escolha um número maior ou igual ao anterior:"))

if SomaDados < fase_inicial_n1:
    print('Soma menor')
elif SomaDados > fase_inicial_n2:
    print('Soma maior')
else:
    print('Soma no meio')

print(Dinheiro)

fase_chutes_n1 = int(input("Qte de chutes para comprar(1 chute/1 dinheiro):"))

Dinheiro-=fase_chutes_n1
Chutes=fase_chutes_n1

while Chutes > 0:
    fase_chutes_chute = int(input("Chute um número:"))
    if fase_chutes_chute == SomaDados:
        Dinheiro+=5*Dinheiro
        break
    else:
        Chutes-=1

print("Você terminou o jogo com {0} dinheiros" .format(Dinheiro))