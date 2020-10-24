import random
dinheiro= 100
print("Voce tem {0}".format( dinheiro))

while dinheiro>0:
    aposta = int(input("quanto quer apostar?"))
    if aposta == 0:
        break
    perg = input('A aposta é numero ou paridade? ')
    if perg == 'n':
        resp = random.randint(1,36)
        chute = int(input('Escreva um numero entre 1 e 36'))
        if chute == resp:
            dinheiro+=aposta*35
            print("Voce tem {0}".format( dinheiro))
        else:
            dinheiro-= aposta
            print("Voce tem {0}".format( dinheiro))
    elif perg == 'p':
        par_impar = input("Voce quer apostar em par ou impar")
        a = random.randint(1,36)
        if a%2 == 0:
            a = 'par'
        else:
            a = 'impar'
        if par_impar == 'p'and a == 'par':
            dinheiro+=aposta
            print("Voce tem {0}".format( dinheiro))
        elif par_impar == 'i' and a == 'impar':
            dinheiro+=aposta*35
            print("Voce tem {0}".format( dinheiro))
        else:
            dinheiro-=aposta
            print("Voce tem {0}".format( dinheiro))
            
        
            
        
    
    
