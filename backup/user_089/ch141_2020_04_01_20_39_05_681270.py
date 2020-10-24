import random
JOGAR = True

soma = 0
dinheiro = 1000
while JOGAR == True:
    
    quer = input("Quer apostar?")
    if quer == "não":
        
        break
    else:

        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        soma = d1+d2
        chute = int(input("Qual o valor da soma?"))
        dinheiro = dinheiro - 30
        if chute == soma:
            dinheiro = dinheiro + 50
            
        else:
            
            pergunta = input("Quer continuar?")
            if pergunta == "desistir":
                print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
                JOGAR = True
            else:
                dinheiro = dinheiro - 20
                chute2 = int(input("Qual o valor da soma?"))
                if chute2 == soma:
                    dinheiro = dinheiro + 50
                else:
                    print(d1)
                    
                    pergunta2= input("Quer continuar?")
                    if pergunta2 == 'desistir':
                        print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
                        JOGAR = True
                    else:
                        dinheiro = dinheiro -10
                        chute3 = int(input("Qual o valor da soma?"))
                        if chute3 == soma:
                            JOGAR = True
                        else:
                            JOGAR = True