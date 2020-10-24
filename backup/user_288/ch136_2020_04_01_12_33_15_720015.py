import random
r1 = random.randint (1,6)
r2 = random.randint (1,6)
r3 = random.randint (1,6)
soma = r1 + r2 + r3
dinheiro = 10
while dinheiro != 0:
    print ('Você tem R$ {0}'. format (dinheiro))
    dica = input ('Quer uma dica? (s/n)')
    if dica == 's':
        dinheiro = dinhiero -1
        n1 = int(input('Escolha um número:'))
        n2 = int(input('Escolha um número:'))
        n3 = int(input('Escolha um número:'))
        if soma == n1 or soma == n2 or soma == n3:
            print ('Está entre os 3')
        else:
            print ('Não está entre os 3')
    else:
        while dinheiro > 0:
            print (dinheiro)
            chute = int (input('Escolha um número:'))
            soma = r1 + r2 + r3
            if chute == soma:
                dinheiro = dinheiro * 5
        break
            else:
                dinheiro =dinheiro - 1               
if dinheiro > 0:
    print ('Você ganhou o jogo com{0} dinheiros!'.format (dinheiro))
else:
    print ('Você perdeu!')