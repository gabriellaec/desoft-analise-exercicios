import random
d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
d3 = random.randint(1, 6)
s = d1 + d2 + d3
caixa = 10
print('Disponivel em caixa: {} dinheiros'.format(caixa))
dica = input('Quer uma dica? ')
while caixa > 0:
    if dica == 'sim':
        print('Disponivel {} dinheiros'.format(caixa))
        caixa = caixa - 1
        n1 = int(input('Escolha um número '))
        n2 = int(input('Escolha um número '))
        n3 = int(input('Escolha um número '))
        if s == n1 or s == n2 or s == n3:
            print('Está entre os 3')
        else:
            print('Não está entre os 3')
        dica = input('Quer uma dica? ')
    if dica == 'não':
        print('Disponivel {} dinheiros'.format(caixa))
        c = int(input('Chute um número '))
        if s == c:
            print('Você ganhou o jogo com {} dinheiros!'.format(caixa*4))
        else:
            caixa = caixa - 1
if caixa <= 0:
    print('perdeu')