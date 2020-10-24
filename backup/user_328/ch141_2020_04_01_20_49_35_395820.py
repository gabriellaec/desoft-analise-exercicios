from random import randint
din= 1000
while din>0 :
    a=input('Você quer apostar(sim/não)? ')
    if a == 'não':
        print('Você terminou a partida com {0} dinheiros'.format(din))
        break
    else:
    d1= random.randrange(1,7)
    d2= random.randrange(1,7)
    soma= d2 + d1
    chutar= int(input('Comece chutando um número(Custo= 30 dinheiros): '))
    din -= 30
    if soma == 'chutar':
        din += 50
        print('Você terminou a partida com {0} dinheiros'.format(dins))
    else :
        jogue_novamente= input('Você quer continuar ou desistir?' )
        if jogue_novamente == 'desistir':
            print('Você terminou a partida com {0} dinheiros'.format(din))
        else :
            seq= input('Digite na sequência um número para tentar acertar a soma(Custo=20 dinheiros): ')
            din -= 20
            if seq == soma:
                din += 50
                print('Você terminou a partida com {0} dinheiros'.format(din))
            else:
                print('o valor de um dos dados é {0}'.format(d1))
                jogue_novamente= input('Você quer continuar tentando ou quer desistir? ')
                if jogue_novamente == 'desistir':
                    print('Você terminou a partida com {0} dinheiros'.format(din))
                if jogue_novamente == 'continuar':
                    c= int(input('Digite na sequência um número para tentar acertar(Custo= 10 dinheiros): '))
                    din -= 10
                    if soma == c:
                        print('Você terminou a partida com {0} dinheiros'.format(din))
                        din += 50
   
     
            
    
 
