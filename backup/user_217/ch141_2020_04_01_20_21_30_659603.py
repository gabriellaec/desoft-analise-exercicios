import random
mao=1000
game = True
while game:
    pergunta = input('Quer apostar?:')
    if pergunta == 'sim':
        dado1 = random.randint(1,6)
        dado2= random.randint(1,6)
        soma = dado1+dado2
        print(soma)
        mao=mao-30
        aposta = True
        while aposta:
            
            chute=float(input("chute o valor: "))
            if chute == soma:
                mao=mao+50
                
                aposta = False

            if chute != soma:
                pergunta_2=input("Vc desistir ou continua?: ")

                if pergunta_2 == "desistir":
                    aposta = False

                else:
                    mao=mao-20
                    parte_2=True
                    while parte_2:
                        
                        chute=float(input("chute o valor: "))
                        if chute == soma:
                            mao=mao+50
                            print(mao)
                            parte_2=False
                            aposta = False
                            
                        if chute != soma:
                            print(dado1)
                            pergunta_2=input("Vc desistir ou continuar?: ")

                            if pergunta_2 == "desistir":
                                parte_2=False
                                aposta = False

                            if pergunta_2 == "continuar":
                                mao=mao-10
        print('Você terminou a partida com {0} dinheiros'.format(mao))


    if pergunta == "não":
        game = False