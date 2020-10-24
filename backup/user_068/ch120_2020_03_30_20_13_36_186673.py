import random as rnd
a = 100

while a > 0:
    print(a)
    aposta = int(input())
    
    if aposta == 0
        break
        
    num_ou_par = input()

    if num_ou_par == 'n':
        num = int(input())
        sorteio = rnd.randit(0, 36)
        if num == sorteio:
            dinheiro += aposta * 35
        else:
            dinheiro -= aposta
    elif num_ou_par == 'p':
        par  = input()
        sorteio = rnd.randit(0, 36)
        if par == 'p' and sorteio%2 == 0:
            dinheiro += aposta
        elif par == 'p'  and sorteio%2 !=0:
            dinheiro += aposta
        else:
            dinheiro-=aposta
        