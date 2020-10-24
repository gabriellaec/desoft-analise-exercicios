from random import randint
a=randint (1,10)
b=randint (1,10)
c=a+b

fichas=10

x=int(input('Diga um número:  '))
y=int(input('Diga um número maior ou igual ao anterior:  '))

if c<x:
    print('Soma menor')
elif c>y:
    print('Soma maior')
else:
    print('Soma no meio')
    
print(fichas)
chute=1

aposta=int(input('Quantos chutes quer comprar?   '))
fichas-=aposta*chute
i=int(input('Chute um número:  '))
j=0

while j<=len(aposta):
    print (i)
    j+=1
    if i==c:
        fichas+=5*fichas
        break
    elif i!=c:
        fichas=fichas
        break
print('Você terminou o jogo com', +fichas, 'dinheiros')