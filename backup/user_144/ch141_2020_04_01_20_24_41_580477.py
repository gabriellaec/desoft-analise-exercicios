import random 
dinheiros = 1000
while True:
    print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
    if dinheiros < 0 and dinheiros == 0:
        break
    pergunta = input("jogar ?")
    
    if pergunta == 'não':
        break
    elif pergunta == 'sim':
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        soma = dado1 + dado2
        num_chute = int(input(" valor "))
        dinheiros -= 30
        if num_chute == soma:
            dinheiros += 50
            
        pergunta2 = input("Continuar?")
        while pergunta2 != "desisitr" :
            num_chute = int(input(" valor "))
            dinheiros -= 20
            if num_chute == soma:
                dinheiros += 50
                
            else:
                print(f"Valor de um dos dados é {dado1}")
                pergunta2 = input("Continuar?")
                if pergunta2 == 'desistir' :
                        break
                    
                elif pergunta2 == 'continuar':
                    num_chute = int(input(" valor "))
                    dinheiros =- 10
                    if num_chute == soma:
                        dinheiros += 50