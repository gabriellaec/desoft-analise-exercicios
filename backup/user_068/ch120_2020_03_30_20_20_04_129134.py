import random as rnd
a = 100

while a > 0:
    print(a)
    aposta = int(input())
    
    if aposta == 0:
        break
        
    num_ou_par = input()

    if num_ou_par == 'n':
        num = int(input())
        sorteio = rnd.randint(0, 36)
        if num == sorteio:
            a += aposta * 35
        else:
            a -= aposta
    elif num_ou_par == 'p':
        par  = input()
        sorteio = rnd.randint(0, 36)
        if par == 'p' and sorteio%2 == 0:
            a += aposta
        elif par == 'i'  and sorteio%2 !=0:
            a += aposta
        else:
            a -=aposta
        