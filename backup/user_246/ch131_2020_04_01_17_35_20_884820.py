import random
dados=random.randint(1,10)+random.randint(1,10)
fichas=10

x=int(input('numero'))
y=int(input('numero'))
if x+y<dados:
    print("Soma menor")
elif x+y>dados:
    print("Soma maior")
else:
    print("Soma no meio")

print(fichas)
c=int(input('chutes'))
fichas=fichas-c
while c!=0:
    chute=int(input('Seu chute'))
    if chute==dados:
        fichas=fichas*6
        c=0
    else:
        c=c-1
print("Você terminou o jogo com {} dinheiros",format(fichas))