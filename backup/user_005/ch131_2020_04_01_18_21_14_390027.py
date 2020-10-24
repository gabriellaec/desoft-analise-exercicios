import random 
dado_1 = random.randint(1,10)
dado_2 = random.randint(1,10)
soma = dado_1 + dado_2 
dinheiro = 10
n = int(input('digite um numero:'))
numero2 = int(input('digite outro numero, maior ou igual ao anterior:')
if soma < n: #esta dizendo que tem erro aqui, mas eu não sei o que está errado, ja tentei de tudo
    print ('Soma menor') 
elif soma > numero2:
    print ('Soma maior')             
else:
    print ('soma no meio')
dinheiro = 10 
chutes = int(input('quantos chutes quer comprar?:'))       
novo_dinheiro -= chutes
while chutes > 0:
    print ('voce ainda possui {0} chutes'.format(chutes)
    chute = int(input('chute:')
    if chute == soma:
        dinheiro_F = novo_dinheiro + 5*novo_dinheiro
        break
    else:
        chute = chutes - 1
if chutes == 0:
    dinheiro_F = dinheiro
print ('Você terminou o jogo com {0} dinheiro'.format(dinheiro_F)) 
