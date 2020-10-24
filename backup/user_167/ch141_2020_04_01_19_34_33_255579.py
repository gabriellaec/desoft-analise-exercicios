from random import randint
import random 
i=1000
som=0
a=input("quer apostar?:")
while a != "não":
    r1 = random.randint(1,6) 
    r2=random.randint(1,6)
    som=(r1+r2)
    b=("adivinhe o numero da soma dos dados:")
    if b == som:
        i+=20
        print('Você terminou a partida com {0} dinheiros'.format(i))
    else:
        i-=50
        print('Você terminou a partida com {0} dinheiros'.format(i))
        c=input("quer continuar tentando ou quer desistir?:")
        if c == "desistir":
            break
        else:
            b=("adivinhe o numero da soma dos dados:")
            i-=20
            print('Você terminou a partida com {0} dinheiros'.format(i))
            if  b == som:
                i+=50
                print('Você terminou a partida com {0} dinheiros'.format(i))
            else:
                print(r1)
                c=input("quer continuar tentando ou quer desistir?:")
                if c == "desistir":
                    break
                if c == "continuar":
                    b=("adivinhe o numero da soma dos dados:")
                    i-=10
                    print('Você terminou a partida com {0} dinheiros'.format(i))
                    if  b == "som":
                        i+=50
                        print('Você terminou a partida com {0} dinheiros'.format(i))
                    
                
        
        
   
    
    