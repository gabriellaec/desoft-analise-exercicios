from random import randint

lancamento = randint(1,6) + randint(1,6) + randint(1,6)
dinheiros = 10
print(lancamento)

while dinheiros > 0:
    
    print(dinheiros)
    quer_dica = input()
    
    if quer_dica == 'não': break
    if quer_dica != 'sim': continue
    
    dinheiros -= 1
    
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    
    if n1 == lancamento or n2 == lancamento or n3 == lancamento:
        print('Está entre os 3')
    else: print('Não está entre os 3')

while True:
    
    print(dinheiros)
    
    if dinheiros == 0:
        print('Você perdeu!')
        break
    
    chute = int(input())
    
    if chute == lancamento:
        dinheiros += dinheiros * 5
        print('Você ganhou o jogo com %d dinheiros!' % dinheiros)
        break
    
    else:
        dinheiros -= 1
    
    
    