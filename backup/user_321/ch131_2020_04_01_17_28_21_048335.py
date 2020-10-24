import random
d1 = random.randint(1, 10)
d2 = random.randint(1, 10)
soma = d1+d2

print('Fase de Dicas')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número, maior ou igual ao ultimo: '))
if n1 > soma:
    print ('Soma menor')
elif n2 < soma:
    print ('Soma maior')
else:
    print ('Soma no meio')
dinheiro = 10 
print('Você tem {0} dinheiros.'.format(dinheiro))
c = int(input('Quantos chutes quer comprar? '))
dinheiro -= c
while True:
    print('Você ainda tem {0} chutes'.format(c))
    chute = int(input('Chute: '))
    if chute != soma:
        c -= 1
    else:
        c -= 1
        dinhero_f = dinheiro + c + 5*c
        break
print('Você terminou o jogo com {0} dinheiros'.format(dinheiro_f))