import random

dinheiros=10
soma=0

def soma_dados():
    dado1=random.randint(1,10)
    dado2=random.randint(1,10)
    soma=dado1 + dado2
    return soma

def dicas():
    soma=soma_dados()
    pergunta=int(input("Diga um número de 1 a 10: "))
    pergunta2=int(input("Diga um número maior ou igual ao que disse anteriormente: "))
    if soma<pergunta:
        print("Soma menor")
    elif soma>pergunta2:
        print("Soma maior")
    else:
        print("Soma no meio")

def chutes(soma):
    global dinheiros
    print(dinheiros)
    chute=int(input("Quantos chutes quer comprar?"))
    dinheiros-=chute
    while chute>0:
        resposta=int(input("Qual a soma dos dados? "))
        if resposta==soma:
             print("Você acertou!")
             dinheiros+=dinheiros*5
        else:
            chute-=1

dicas()
chutes(soma)
print("Você terminou o jogo com",dinheiros,"dinheiros")