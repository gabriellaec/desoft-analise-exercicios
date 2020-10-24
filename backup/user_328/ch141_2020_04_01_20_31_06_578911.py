import randon
din= 1000
while a == 'sim':
    a=input('Você quer apostar(sim/não)? ')
    d1= random.randrange(1,7)
    d2= random.randrange(1,7)
    soma= d2 + d1
    chutar= int(input('Comece chutando um número(Custo= 30 dinheiros): '))
    if soma == 'chutar':
        din += 20
    elif soma != 'apostar':
        jogue_novamente= input('Você quer continuar ou desistir?' )
        if jogue_novamente == 'desistir':
            apostar == 'sim'
        elif jogue_novamente != 'sim':
            seq= input('Digite na sequência um número para tentar acertar a soma(Custo=20 dinheiros): ')
            if seq == soma:
                din += 50
            else:
                print('o valor de um dos dados é {0}'.format(d1))
                jogue_novamente= input('Você quer continuar tentando ou quer desistir? ')
                if jogue_novamente == 'desistir':
                    aposta == 'sim'
                if jogue_novamente == 'continuar':
                    c= int(input('Digite na sequência um número para tentar acertar(Custo= 10 dinheiros): '))
                    if soma == c:
                        din -= 10
    if din < 0:
        break    
    print('Você terminou a partida com {0} dinheiros'.format(din))  
     
            
    
 
