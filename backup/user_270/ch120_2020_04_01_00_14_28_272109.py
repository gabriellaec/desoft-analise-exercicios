import random
dinheiro = 100
k = True
while k :
    if dinheiro > 0 :
        print("Você possui {0} dinheiros".format(dinheiro))
        aposta =int(input("Quanto de dinheiro você quer apostar? "))
        if aposta != 0:
            tipo_de_aposta = input('Que tipo de aposta você quer fazer? Digite n para número e p para paridade. ')
            if tipo_de_aposta == 'n' :
                num_ale = random.randint(0,36)
                num_dig = int(input('Digite o seu número: '))
                if num_dig == num_ale :
                    dinheiro = dinheiro + num_dig*aposta
                else:
                    dinheiro = dinheiro - aposta
            if tipo_de_aposta == 'p' :
                num_ale = random.randint(0,36)
                guess = 'p'
                if num_ale % 2 == 0 :
                    guess = 'p'
                else:
                    guess = 'i'
                user_guess = input('Chute p para par e i para impar ')
                if user_guess == guess :
                    dinheiro = dinheiro + aposta
                else:
                    dinheiro = dinheiro - aposta
        else:
            k = False
    else:
        k = False