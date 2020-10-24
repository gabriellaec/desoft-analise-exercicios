import random
d=1000
while d>0:
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    a=input("vc quer apostar?")
    if a=="não":
        break
    else:
        soma=dado1+dado2
        chute=int(input("chute o valor dos dados"))
        if chute==soma:
            d=d+20
            print('Você terminou a partida com {0} dinheiros'.format(d))
        else:
            print(soma)     
            d=d-30
            print('Você terminou a partida com {0} dinheiros'.format(d))
            b=input("desistir ou continuar?")
            if b=='desistir':
                continue
            elif b=='continuar':
                chute2=input("tente novamente")
                if chute2==soma:
                    d=d+30
                    print('Você terminou a partida com {0} dinheiros'.format(d))
                else:
                    print(soma)
                    d=d-20
                    print('Você terminou a partida com {0} dinheiros'.format(d))
                    c=input("desistir ou continuar?")
                    if c=='desistir':
                        continue
                    elif c=='continuar':
                        chute3=int(input("tente novamente")
                        if chute3==soma:
                            
                        
                    
                    
            

               
           
                  
        
