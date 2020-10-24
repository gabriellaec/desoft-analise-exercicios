import random

jogo = True

while jogo == True:
    perguntainicial = input("Você quer jogar?(s/n) ")
    if perguntainicial == 'n':
        jogo = False
    elif perguntainicial == 's':
        dinheiros = 100
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        somadados = dado1 + dado2
        print('Você tem 100 dinheiros. Agora você gastará 30 dinheiros')
        primeiraperguntajogo = input('Qual a soma dos dados?(2 a 12) ')
        if primeiraperguntajogo == somadados:
            dinheiros = dinheiros-30+50
            print("Você terminou a partida com {0} dinheiros".format(dinheiros))
            jogo = False
        else:
            dinheiros = dinheiros-30
            segundaperguntajogo = input("Você vai continuar tentando ou vai desistir? ")
            if segundaperguntajogo == "desistir":
                print("Você terminou a partida com {0} dinheiros.".format(dinheiros))
                jogo = False
            else:
                print("Você está com {0} dinheiros. Você apostará mais 20 dinheiros".format(dinheiros))
                terceiraperguntajogo = input("Qual a soma dos dados?(2 a 12) ")
                if terceiraperguntajogo == somadados:
                    dinheiros = dinheiros - 20 + 50
                    print("Você terminou a partida com {0} dinheiros".format(dinheiros))
                    jogo = False
                else:
                    dinheiros = dinheiros - 20
                    print("O número de um dos dados é: {0}".format(dado1))
                    quartaperguntajogo = input("Você vai continuar tentando ou vai desistir? ")
                    if quartaperguntajogo == "desistir":
                        print("Você terminou a partida com {0} dinheiros.".format(dinheiros))
                        jogo = False
                    else:
                        print("Você está com {0} dinheiros. Você apostará mais 10 dinheiros.".format(dinheiros))
                        quintaperguntajogo = input("Qual a soma dos dados?(2 a 12) ")
                        if quintaperguntajogo == somadados:
                            dinheiros = dinheiros - 10 + 50
                            print("Você terminou a partida com {0} dinheiros".format(dinheiros))
                            jogo = False
                        else:
                            dinheiros = dinheiros - 10
                            print("Você terminou a partida com {0} dinheiros".format(dinheiros))
                            jogo = False
    jogo = False