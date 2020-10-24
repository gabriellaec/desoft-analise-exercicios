import random
dinheiros = 100
while(dinheiros > 0):
    print(dinheiros)
    aposta = int(input("entre com a aposta: "))
    if (aposta == 0):
        break
    else:
        sorteio = random.randint(0, 36)
        y = input("é um numero ou paridade?(n/p)")
        if y == "n":
            num = int(input("entre com um numero de 1 a 36:"))
            if num == sorteio:
                dinheiros += aposta*35
            else:
                dinheiros -= aposta
        if y == "p":
            num = input("par ou impar? (p/i) ")
            if num == "p":
                if sorteio%2 == 0:
                    dinheiros += aposta
                else:
                    dinheiros -= aposta
            if num == "i":
                if sorteio%2 != 0:
                    dinheiros += aposta
                else:
                    dinheiros -= aposta