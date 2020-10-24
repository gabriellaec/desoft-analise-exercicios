import random
dinheiro = 100
while (dinheiro > 0):
    pares = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
    impares = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
    print("Você tem {0} dinheiros".format(dinheiro))
    continuar = input("Deseja continuar? (s/n) ")
    if continuar == "s":
        valoraposta = int(input("Escolha um valor para apostar: "))
        if valoraposta > dinheiro or valoraposta <= 0:
            print("Valor inválido. Aposte entre 1 e seu dinheiro")
        else:
            tipoaposta = input("Deseja apostar por número (digite 'n') ou por paridade (digite 'p' para par e 'i' para ímpar): ")
            if tipoaposta  == 'n':
                apostaentre = int(input("Escolha um número entre 1 e 36: "))
                if apostaentre in range(1,36):
                    resultado1 = random.randint(0,36)
                    print(resultado1)
                    if apostaentre == resultado1:
                        dinheiro = dinheiro + valoraposta*35
                        print("Parabéns! Você ganhou")
                    else:
                        print("Sinto muito, não foi dessa vez. Tente novamente")
                        dinheiro = dinheiro - valoraposta
                else:
                    print("Resposta inválida.")
            elif tipoaposta == 'p':
                resultado2 = random.randint(0,36)
                print(resultado2)
                if resultado2 in pares:
                    print("Parabéns! Você ganhou")
                    dinheiro = dinheiro + valoraposta
                else:
                    print("Sinto muito, você perdeu. Tente novamente")
                    dinheiro = dinheiro - valoraposta
            elif tipoaposta == 'i':
                resultado2 = random.randint(0,36)
                if resultado2 in impares:
                    print("Parabéns! Você ganhou")
                    dinheiro = dinheiro + valoraposta
                else:
                    print("Sinto muito, você perdeu. Tente novamente")
                    dinheiro = dinheiro - valoraposta
            else:
                print("Resposta inválida. Digite 'n', 'p' ou 'i'")
    elif continuar == "n":
        print("Tchau, obrigada por jogar")
        print("Você terminhou com {0} dinheiros".format(dinheiro))
        dinheiro = 0
    else:
        print("Resposta inválida. Responda 's' ou 'n'")