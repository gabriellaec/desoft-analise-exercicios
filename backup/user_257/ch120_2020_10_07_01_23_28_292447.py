import random
dinheiro=100
print("Ola jogador 1, voce possui {0} dinheiros".format(dinheiro))

while dinheiro > 0:
    aposta=int(input("faça sua aposta: "))
    a= random.randint(0,36)
    print(a)
    #aposta= int(input("Digite sua aposta: "))
    aposta1=input("a aposta é um numero ou paridade? ")
    if aposta == 0:
        dinheiro=0
    else:
        if aposta1 == "n":
            numero_aleatorio= input("digite um numero entre 1 e 36: ")
            if numero_aleatorio == a:
                dinheiro= dinheiro+(35*aposta)
                print("voce ganhou! seu saldo agora é {0}".format(dinheiro))
            else:
                dinheiro= dinheiro - aposta
                print("voce perdeu, seu saldo agora é {0}".format(dinheiro))
        elif aposta1 == "p":
            aposta2= input("voce quer impar ou par? ")
            if aposta2== "i":
                if a%2 == 0:
                    dinheiro= dinheiro - aposta
                    input("voce perdeu, seu saldo agora é {0}".format(dinheiro))
                else:
                    dinheiro= dinheiro + aposta
                    input("voce ganhou! seu saldo agora é {0}".format(dinheiro))
            else:
                if a%2 != 0:
                    dinheiro= dinheiro - aposta
                    input("voce perdeu, seu saldo agora é {0}".format(dinheiro))
                else:
                    dinheiro= dinheiro + aposta
                    input("voce ganhou! seu saldo agora é {0}".format(dinheiro))
