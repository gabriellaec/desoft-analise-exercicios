jogo=True
soma=0
while jogo==True:
    x=int(input("Digite um numero:"))
    if x!=0:
        soma=x+soma
        jogo=True
    elif x==0:
        jogo=False
print (soma)