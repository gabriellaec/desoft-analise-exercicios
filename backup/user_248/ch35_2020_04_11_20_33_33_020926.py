jogo=True
while jogo==True:
    x=int(input("Digite um numero:"))
    soma=0
    if x!=0:
        soma=x+soma
        jogo=True
    elif x==0:
        jogo=False
print (soma)