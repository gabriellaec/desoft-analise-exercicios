din = 1000
p1=input("Quer apostar?")
if p1=='não':
    print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
while p1=='sim':
    import random
    num1=random.randint(1,6)
    num2=random.randint(1,6)
    s=num1+num2
    chute=int(input("Chute um numero"))
    din=din-30
    if chute==s:
        din=din+50
        print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
    else:
        p2=input("continuar ou desistir?")
        if p2=="desistir":
            print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
        else:
            chute=int(input("Chute um numero"))
            din=din-20
            if chute==s:
                din=din+50
                print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
            else:
        p2=input("continuar ou desistir?")
        if p2=="desistir":
            print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
                

                
            

            
        
        
        
    