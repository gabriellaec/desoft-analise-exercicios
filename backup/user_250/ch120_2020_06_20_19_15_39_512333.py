import random
loop = True
dinheiros = 100
while loop == True:
    print(dinheiros)
    aposta = float(input("Deseja apostar? "))
    if aposta == 0:
        loop = False
    else:
        jogo = input("Qual jogo? ")
        if jogo == 'n':
            num = int(input("Qual número? "))
            sorteio = random.randint(0,36)
            if num == sorteio:
                print("Você ganhou")
                dinheiros = dinheiros + (aposta*35)
                #print(dinheiros)
            else:
                print("Você perdeu")
                dinheiros = dinheiros - aposta
                #print(dinheiros)
        if jogo == 'p':
            paridade = input("'p' ou 'i' ")
            sorteio = random.randint(0,36)
            if sorteio%2 == 0:
                vencer = 'p'
                if vencer == paridade:
                    print("Você ganhou")
                    dinheiros = dinheiros + aposta
                    #print(dinheiros)
                else:
                    print("Você perdeu")
                    dinheiros = dinheiros - aposta
                    #print(dinheiros)
            else:
                vencer = 'i'
                if vencer == paridade:
                    print("Você ganhou")
                    dinheiros = dinheiros + aposta
                    #print(dinheiros)
                else:
                    print("Você perdeu")
                    dinheiros = dinheiros - aposta
                    #print(dinheiros)
                           

    