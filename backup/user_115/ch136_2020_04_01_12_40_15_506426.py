import random as random

d1 = random(1, 6, 1) 
d2 = random(1, 6, 1)
d3 = randome(1, 6, 1)

din=10

def jogo (din, d1, d2, d3):
    print("Você tem", {din}, " dinheiros")
    if (din == 0):
        return print("Você perdeu o jogo!")
    elif (din > 0):
        resp = input(print("Você gostaria de uma dica? sim/nao"))
        if (resp == "sim"):
            din-=1
            ale1 = print(random.range(3, 18, 1))
            ale2 = print(random.range(3, 18, 1))
            ale3 = print(random.range(3, 18, 1))
            if (ale1 or ale2 or ale3 == (d1+d2+d3)):
                print("Está entre um dos 3")
            else:
                print("Não está entre um dos 3")
        resp = " "
        if (resp == "nao"):
            gan = 0
            while (gan == 0):
                print("Você tem ", {din}, "dinheiros")
                if (din == 0):
                    "O seu dinheiro acabou. Pode chutar um número."
                    chute = int(input())
                else:
                    "Você pode adivinhar um número."
                    chute = int(input())
                if ((d1+d2+d3) == chute):
                    din = din*5
                    gan = 1
                    print("Você ganhou o jogo com", {x}, " dinheiros!")
                else: 
                    din-=1