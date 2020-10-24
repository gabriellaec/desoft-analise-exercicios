import random

dinheiro=1000

while dinheiro>0:
    pergunta1=input('Quer apostar?')
    if pergunta1=='não':
    print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
    break

    if pergunta1=='sim':
        dado1=randint(1,6)
        dado2=randint(1,6)
        soma=dado1+dado2
        chute=int(input('Chuta a soma dos dados:'))
        dinheiro-=30
        if chute==soma:
            dinheiro+=50
            print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
        else:
            pergunta2=input('Continua ou desiste?')
            if pergunta2=='desisitir':
                print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
                
            else:
                chute2=int(input('Tente novamente'))
                dinheiro-=20






