import random
cart = 1000
while True:
    print(cart)
    if cart<=0:
        print('Você terminou a partida com {} dinheiros'.format(cart))
        break
    else:
        querapostar = input('Quer apostar? ')
        if querapostar=='não':
            print('Você terminou a partida com {} dinheiros'.format(cart))
            break
        else:
            dado1 = random.randint(1,6)
            dado2 = random.randint(1,6)
            somadados = dado1+dado2
            chute = int(input('Chute um valor: '))
            if chute==somadados:
                cart = cart+20
            else: 
                cart = cart-30
                continuar = input('Quer continuar tentando? ')
                if continuar=='desistir':
                    pass
                else:
                    chute2 = int(input('Chute um valor: '))
                    if chute2==somadados:
                        cart = cart-20+50
                    else: 
                        cart = cart-20
                        print (dado1)
                        continuar2 = input('Quer continuar tentando? ')
                        if continuar2=='desistir':
                            pass
                        elif continuar2=='continuar':
                            chute3 = int(input('Chute um valor: '))
                            if chute3==somadados:
                                cart = cart-10+50
                            else: 
                                cart = cart-10
                        else:
                            pass


            
                

