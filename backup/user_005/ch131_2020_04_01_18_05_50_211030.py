import random 

dado_1 = random.randint(1,10)
dado_2 = random.randint(1,10)
soma = dado_1 + dado_2 
dinheiro = 10
numero = int(input('digite um numero:'))
numero2 = int(input('digite outro numero, maior ou igual ao anterior:')
if soma < numero:
    print ('Soma menor')
elif soma > numero2:
    print ('Soma maior')             
else:
    print ('soma no meio')
dinheiro = 10 
chutes = int(input('quantos chutes quer comprar?:'))       
novo_dinheiro -= chutes
while chutes > 0:
    if chutes == soma:
        dinheiro_F = novo_dinheiro + 5*novo_dinheiro
    else:
        chutes = chutes - 1
if chutes == 0:
    dinheiro_F = dinheiro
Print ('Você terminou o jogo com {0} dinheiro'.format(dinheiro))              