from random import randint 
dinheiros = 1000
while (fichas>0):
    pergunta = input("Você quer apostar? ")
    if pergunta =="não":
        print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
        break
    else:
        dado1 = randint(0,6)
        dado2 = randint(0,6)
        soma = dado1+dado2
        chute1 = int(input("Tente acertar a soma, digite: "))
        dinheiros = dinheiros - 30
        if chute1 == soma: 
            dinheiros = dinheiros + 50
        else: 
            pergunta2 = input("Você quer continuar ou desistir: ")
            if pergunta2=="desistir":
                print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
                break
            else:
                chute2 = int(input("Tente novamente: "))
                dinheiros = dinheiros - 20
                if chute2==soma:
                    fichas = fichas + 50
                else: 
                    print (dado1)
                    pergunta3=input("Sabendo um dado, quer continuar? ")
                    if pergunta3=="desistir":
                        print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
                        break
                    if pergunta3=="continuar":
                        chute3=int(input("Tente novamente: "))
                        dinheiros = dinheiros - 10
                        if chute3 ==soma:
                            print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
                            dinheiros = dinheiros + 50
                            break
                        
                        
    