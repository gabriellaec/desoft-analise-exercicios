import random
soma_dados= (random.randint(1,6)+random.randint(1,6)+random.randint(1,6))
dinheiro = 10
perdeu = False
quer_dica =True
while perdeu == False:
    while quer_dica == True:
        print(dinheiro)
        if dinheiro < 1:
            perdeu = True
            quer_dica = False
            print("Você perdeu!")
        else:
            quer_dica = True
            d = input('Voce quer uma dica? ')
            if d == 'sim':
                dinheiro -= 1
                quer_dica = True
                n1 = int(input('Entre com o primeiro numero: '))
                n2 = int(input('Entre com o segundo numero: '))
                n3 = int(input('Entre com o terceiro numero: '))
                if n1 == soma_dados or n2 == soma_dados or n3 == soma_dados:
                    print("Está entre os 3")
                else:
                    print("Não está entre os 3")
            else:
                quer_dica = False
    while perdeu == False or dinheiro > 1:
        print(dinheiro)
        if dinheiro < 1:
            perdeu = True
            print("Você perdeu!")
        else:
            c = input('Chute um numero: ')
            if c == soma_dados:
                dinheiro = dinheiro + dinheiro*5
                print("Você ganhou o jogo com {} dinheiros!" .format(dinheiro))
                perdeu = True
            else:
                dinheiro -= 1
            

        
        

