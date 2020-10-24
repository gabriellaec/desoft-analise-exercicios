import random
dado1=random.randint(1, 10)
dado2=random.randint(1, 10)
soma=dado1+dado2
quantia=10
numero1=int(input("Digite um número"))
numero2=int(input("Digite outro número"))
if soma < numero1:
    print("Soma menor")
elif soma >numero2:
    print("Soma maior")
else:
    print("Soma no meio")
print("Voce tem {0} dinheiros".format(quantia))
nchutes=int(input("Digite quantos chutes voce quer comprar:"))
quantia=quantia-nchutes
naoacertou=True
while nchutes>0 and naoacertou:
    chute=input("Chute um valor")
    if chute==soma:
        quantia=quantia+quantia*5
        print("Você terminou o jogo com {0} dinheiros".format(quantia))
        naoacertou=False
    else:
        chute=chute-1
print("Você terminou o jogo com {0} dinheiros".format(quantia))    
    
