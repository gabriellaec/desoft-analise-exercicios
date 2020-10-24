import random
dados = random.randint(2,21)
dinheiro = 10
numero1 = int(input("escolha um numero de 0 a 10 "))
numero2 = int(input("Escolha um numero maior ou igual ao anterior, também de 0 a 10 "))
while numero1 < numero2:
    numero2 = int(input("numero menor, tente de novo "))
    
if dados < numero1:
    print("soma menor")
if dados > numero2:
    print("soma maior")
else:
    print("soma no meio")

while dados != numero1 and dados != numero2:
    print("voce tem {0} dinheiros".format(dinheiro))
    chutes = int(input("quantos chutes você quer comprar?").format(dinheiro))
    dinheiro_restante = dinheiro - chutes
    while chutes >0 :
        numero1 = int(input("escolha um numero de 0 a 10 "))
        numero2 = int(input("Escolha um numero diferente, também de 0 a 10 "))
        if dados < numero1:
            print("soma menor")
        if dados > numero2:
            print("soma maior")
        else:
            print("soma no meio")
        chutes = -1

