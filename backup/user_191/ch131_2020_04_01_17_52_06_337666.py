import random
d1=random.randint(1,10)
d2=random.randint(1,10)
din=10
chute1=int(input('Fale um número: '))
chute2=int(input('Fale outro número(maior ou igual o anterior): '))
soma=d1+d2
if soma<chute1:
    print('Soma menor')
elif soma>chute2:
    print('Soma maior')
else:
    print('Soma no meio')
print('Seu dinheiro é:{}'.format(din))
q=int(input('Quantos chutes deseja comprar?'))
din=din-q
while q>0:
    adivinha=int(input('Dê seu chute: '))
    if adivinha==soma:
        din=din+5*din
        break
    else:
        q=q-1
print('Você terminou com {} dinheiros'.format(din))