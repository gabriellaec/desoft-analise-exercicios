import random
dinheiros = 1000
partida = True
while dinheiros != 0 and partida:
    print("Início")
    print("Você tem {0} dinheiros.".format(dinheiros))
    pergunta1 = input("Você quer apostar?: (Digite sim ou não)")
    if pergunta1 == "sim":
        Dado1 = random.randint(1,6)
        Dado2 = random.randint(1,6)
        soma_dos_dados = Dado1 + Dado2
        pergunta2 = input("Qual o seu chute para o valor da soma dos dados?: ")
        dinheiros = dinheiros - 30
        if pergunta2 == soma_dos_dados:
            dinheiros = dinheiros + 50
            print("Você acertou!")
            print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
            partida = True
        elif pergunta2 != soma_dos_dados:
            print("Você errou")
            pergunta3 = input("Você deseja continuar ou vai desistir?: (Digite continuar ou desistir)")
            if pergunta3 == "desistir":
                partida = True
            elif pergunta3 == "continuar":
                dinheiros = dinheiros - 20 
                pergunta4 = input("Qual o seu chute para o valor da soma dos dados?: ")
                if pergunta4 == soma_dos_dados:
                    dinheiros = dinheiros + 50
                    print("Você acertou!")
                    print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
                    partida = True
                elif pergunta4 != soma_dos_dados:
                    print("Você errou")
                    print("Esse é o valor de um dos dados: {0}.".format(Dado1))
                    pergunta5 = input("Você deseja continuar ou vai desistir?: (Digite continuar ou desistir)")
                    if pergunta5 == "desistir":
                        partida = True
                    elif pergunta5 == "continuar":
                        dinheiros = dinheiros - 10
                        pergunta6 = input("Qual o seu chute para o valor da soma dos dados?: ")
                        if pergunta6 == soma_dos_dados:
                            print("Você acertou!")
                            print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
                            dinheiros = dinheiros + 50
                            partida = True
                        elif pergunta6 != soma_dos_dados:
                            print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
                            partida = True

    elif pergunta1 == "não":
        print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
    break
    