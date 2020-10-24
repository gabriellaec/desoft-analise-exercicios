from random import randint
a=randint (1, 10)
b=randint (1, 10)
c=a+b
dinheiro=10

x=int(input('digite um numero: '))
y=int(input('digite um numero maior ou igual ao anterior: '))
if c<x:
    print ("Soma menor")
elif c>y:
    print("Soma maior")
else:
    print ("Soma no meio")

print (dinheiro)
n=int(input('Quantos chutes deseja comprar?: '))
while n<n+1:
        p=int(input('Qual a soma: '))
        if p==c:
            dinheiro=(dinheiro-n)*6
            print (dinheiro)
        elif p!=c:
             p=int(input('Qual a soma: '))

print ("Você terminou o jogo com", + dinheiro, + "dinheiros")