import random
dado1 = random.randint(1,10)
dado2 = random.randint(1,10)
soma = dado1+dado2
dinheiro = 10
while True:
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    if soma<num1:
        print("Soma menor")
    elif soma>num2:
        print("Soma maior")
    else:
        print("Soma no meio")
    break
print("Você tem {0} dinheiros disponíveis".format(dinheiro))
num_chutes = int(input("Quantos chutes você quer comprar? "))
dinheiro-=num_chutes
while True:
    if num_chutes==0:
        break
    else:
        chute = int(input("Qual foi a soma dos dados? "))
        if chute == soma:
            X = dinheiro+dinheiro*3
            break
        else:
            num_chutes-=1
print("Você terminou o jogo com {0} dinheiros".format(X))