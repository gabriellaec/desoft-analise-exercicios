import random as rnd

a = 10
while a > 0:
    dado1 = rnd.randint(0, 6)
    dado2 = rnd.randint(0, 6)
    dado3 = rnd.randint(0, 6)
    soma = dado1 + dado2 + dado3

    b = input('Você quer uma dica? ')
    
    if b == 'sim':
        p1 = int(input("número1:")
        p2 = int(input("número2:")
        p3 = int(input("número3 ")
        a -= 1
            if soma == p1 or soma == p2 or soma == p3:
                 print('Está entre os 3')
            else:
                 print('Não está entre os 3')
                 
            b = input('Você quer uma dica? ')
    if b == 'não':
        print(a)
        if a == 0:
            break
        else:
            num = input('Chute um número')
            if num == soma:
                a = (a * 5) + a
                print('Você ganhou o jogo com {0} dinheiros!".format(a)
                break
            else: 
                 a -= 1 
    if a == 0:
        print("Você perdeu!)
        
    aposta = int(input())
    
    if aposta == 0:
        break
        
    