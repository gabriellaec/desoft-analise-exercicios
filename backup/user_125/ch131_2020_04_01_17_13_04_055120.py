import random 
a=int(input('me diga um número '))
b=int(input('me diga outro número'))
soma1= a+b 
dado1 =random.randint(1,10)
dado2 = random.randint(1,10)
soma2= dado1+dado2 
dinheiros = 10
if soma2>a:
    print ('soma menor')
elif soma2>b:
    print ('soma menor')
elif soma2==soma1:
    print ('soma no meio')
c=int(input('quantos chutes você quer fazer ?'))
chutes =c
dinheiros = dinheiros-chutes
jogo=True
while chutes>0:
    d=int(input('Qual número você acha que é'))
    chutes -=1
    if d==soma2:
        print('você ganhou')
        dinheiros= (dinheiros-chutes)+(dinheiros-chutes)*5
        print ('Você terminou o jogo com '+ dinheiros)
        jogo=False
    else:
        print('você perdeu')
    if chutes==0:
        print ('acabaram seus chutes')
        print ('Você terminou o jogo com '+ str(dinheiros)+ 'dinheiros')
        jogo=False