import random
mao=1000
game = True
while game:
    pergunta_inicial = input('Quer apostar?:')
    if pergunta_inicial == 'sim':
        dado_1 = random.randint(1,6)
        dado_2= random.randint(1,6)
        soma_dados = dado_1+dado_2
        print(soma_dados)
        mao=mao-30
        aposta = True
        while aposta:

            chute=float(input("chute um valor: "))
            if chute == soma_dados:
                mao=mao+50
                aposta = False

            if chute != soma_dados:
                pergunta_meio=input("desistir ou continua?: ")

                if pergunta_meio == "desistir":
                    aposta = False
                else:
                    mao=mao-20
                    metade=True
                    while metade:

                        chute=float(input("chute o valor: "))
                        if chute == soma_dados:
                            mao=mao+50
                            print(mao)
                            metade=False
                            aposta = False

                        if chute != soma_dados:
                            print(dado_1)
                            pergunta_emio=input("Vc desistir ou continuar?: ")

                            elif pergunta_meio == "desistir":
                                metade=False
                                aposta = False

                            elif pergunta_meio == "continuar":
                                mao=mao-10
        print('Você terminou a partida com {0} dinheiros'.format(mao))


    if pergunta == "não":
        game = False