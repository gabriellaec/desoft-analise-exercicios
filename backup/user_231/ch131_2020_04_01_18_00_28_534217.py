import random
s=random.randit(2,20)
n1=int(input('Digite um numero:'))
n2=int(input('Digite um numero maior ou igual:'))
if s<n1:
    print('Soma menor')
if s>n2:
    print('Soma maior')
else:
    print('Soma no meio')
d=10
print('Voce tem {} dinheiros'.format(d))
q=int(input('Quantos chutes voce quer comprar?'))
d=d-q
c=int(input('Qual é o seu chute?'))
while c!=s and q>0:
    q= q-1
    c= int(input('Errou tente novamente:'))
if s==c:
    d= d+ 5*d
print('Você terminou o jogo com {} dinheiros'.format(d))