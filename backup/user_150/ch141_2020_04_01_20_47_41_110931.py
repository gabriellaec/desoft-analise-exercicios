import random

jogo = True
dinheiros = 1000
while jogo == True:
    perguntainicial = input("Você quer jogar?(s/n) ")
    if perguntainicial == 'n':
        jogo = False
    elif perguntainicial == 's':
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        somadados = dado1 + dado2
        print('Você tem 1000 dinheiros. Agora você gastará 30 dinheiros')
        primeiraperguntajogo = int(input('Qual a soma dos dados?(2 a 12) '))
        if primeiraperguntajogo == somadados:
            dinheiros = dinheiros-30+50
            print("Você terminou a partida com {0} dinheiros".format(dinheiros))
        else:
            dinheiros = dinheiros-30
            segundaperguntajogo = int(input("Você vai continuar tentando ou vai desistir? "))
            if segundaperguntajogo == "desistir":
                print("Você terminou a partida com {0} dinheiros.".format(dinheiros))
            else:
                print("Você está com {0} dinheiros. Você apostará mais 20 dinheiros".format(dinheiros))
                terceiraperguntajogo = int(input("Qual a soma dos dados?(2 a 12) "))
                if terceiraperguntajogo == somadados:
                    dinheiros = dinheiros - 20 + 50
                    print("Você terminou a partida com {0} dinheiros".format(dinheiros))
                else:
                    dinheiros = dinheiros - 20
                    print("O número de um dos dados é: {0}".format(dado1))
                    quartaperguntajogo = input("Você vai continuar tentando ou vai desistir? ")
                    if quartaperguntajogo == "desistir":
                        print("Você terminou a partida com {0} dinheiros.".format(dinheiros))
                    else:
                        print("Você está com {0} dinheiros. Você apostará mais 10 dinheiros.".format(dinheiros))
                        quintaperguntajogo = int(input("Qual a soma dos dados?(2 a 12) "))
                        if quintaperguntajogo == somadados:
                            dinheiros = dinheiros - 10 + 50
                            print("Você terminou a partida com {0} dinheiros".format(dinheiros))
                        else:
                            dinheiros = dinheiros - 10
                            print("Você terminou a partida com {0} dinheiros".format(dinheiros))
    if dinheiros <= 0:
        jogo = False