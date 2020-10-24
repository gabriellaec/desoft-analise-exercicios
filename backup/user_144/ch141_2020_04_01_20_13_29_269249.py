import random 
dinheiro = 1000
while True:
    print(f"Vc tem {dinheiro} dinheiros")
    if dinheiro < 0 and dinheiro == 0:
        break
    pergunta = input("jogar ?")
    
    if pergunta == 'não':
        break
    elif pergunta != 'não':
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        soma = dado1 + dado2
        num_chute = int(input(" valor "))
        dinheiro -= 30
        while num_chute < 1:
            num_chute = int(input(" valor "))
        
        if num_chute == soma:
            dinheiro += 50
            print('Você terminou a partida com {0} dinheiros'.format(dinheiro))

        else:
            pergunta2 = input("Continuar?")
            if pergunta2 == "desisitr" :
                print('Você terminou a partida com {0} dinheiros'.format(dinheiro))

            
            else:
                num_chute = int(input(" valor "))
                dinheiro -= 20
                if num_chute == soma:
                    dinheiro += 50
                    print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
                else:
                    print(f"Valor de um dos dados é {dado1}")
                    pergunta2 = input("Continuar?")
                    if pergunta2 == 'desistir' :
                        print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
                    
                    elif pergunta2 == 'continuar':
                        num_chute = int(input(" valor "))
                        dinheiro =- 10
                        if num_chute == soma:
                            dinheiro += 50
                            print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
                            break