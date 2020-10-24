import random
d=10
a=random.randint(1,10)
b=random.randint(1,10)
soma=a+b


chute=int(input('Chute a soma do dado '))
chute1=int(input('Diga outro numero '))
if soma < chute:
    print('Soma menor')
elif soma>chute1:
    print('Soma maior')
else:
    print('Soma no meio')

print('Você tem {0} dinheiros'.format(d))
nchutes=int(input('quantos chutes quer comprar? '))
d=d-nchutes
while nchutes>0:
    chutefinal=int(input('Chute denovo o valor da soma dos dados: '))
    nchutes=nchutes-1
    if chutefinal==soma:
        d=d+(5*d)
        break
print('Você terminou o jogo com {0}'.format(d))


            