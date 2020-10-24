import random
r1 = random.randint (3,18)
dinheiro = 10
print ('Você tem R$ {0}'. format (dinheiro))
while dinheiro != 0:
    dica = input ('Quer uma dica? (s/n)')
    if dica == 's':
        dinheiro -=1
        n1 = int(input('Escolha um número:'))
        n2 = int(input('Escolha um número:'))
        n3 = int(input('Escolha um número:'))
        if r1 == n1 or r1 == n2 or r1 == n3:
            print ('Está entre os 3')
        else:
            print ('Não está entre os 3')
    else:
        print (dinheiro)
        chute = int (input('Escolha um número:)
        if chute == r1:
            dinheiro += dinheiro * 5
            dinheiro = False
        else:
            dinheiro -= 1
    print ('Você ganhou o jogo com{0} dinheiros!'.format (dinheiro))
    else:
        print ('Você perdeu!')
        