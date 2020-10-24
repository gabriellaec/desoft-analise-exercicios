import random
a=random.randint(1,6)
b=random.randint(1,6)
c=random.randint(1,6)
money=10
#fase dicas
print(money)
dica=input("quer dicas?(s/n)")
while dica=='sim':
    money-=1
    q=input("1°numero ")
    w=input("2°numero")
    e=input("3°numero")
    if q+w+e==a or  q+w+e==b or  q+w+e==c:
        print( "Está entre os 3")
    else:
        print("Não está entre os 3")
    dica=input("quer dicas?(s/n)")
#fase chute
print(money)
s=0
while s==0:
    t=input("1°numero ")
    y=input("2°numero")
    u=input("3°numero")
    if t+y+u==a+b+c:
        s+=1
        money=money+(money*5)
        print("Você ganhou o jogo com %d dinheiros!"%(money))
    else:
        money-=money
if money ==0:
    print( "Você perdeu!")