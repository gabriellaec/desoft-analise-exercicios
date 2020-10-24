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
        caixa = caixa - 1
        print('Disponivel {} dinheiros'.format(caixa))
        n1 = int(input('Escolha um número '))
        n2 = int(input('Escolha um número '))
        n3 = int(input('Escolha um número '))
        if s == n1 or s == n2 or s == n3:
                 print('Está entre os 3')
        else:
                 print('Não está entre os 3')
        dica = input('Quer uma dica? ')
    elif dica == 'não':
        print('Disponivel {} dinheiros'.format(caixa))
        chute = int(input('Chute um número'))
        if chute == s:
                 print('Você ganho o jogo com {} dinheiros!'.format(caixa*4))
        else:
                 print('Você perdeu!')
print('Você perdeu!)
                 
    
                 
                 
                 
        
                 
                 
                 
                 
        
                 
        
