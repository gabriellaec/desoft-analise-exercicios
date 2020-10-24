import random
soma = random.randint(3,18)
dinheiro = 10
dica = input ('quer uma dica?' )
while dinheiro > 0 and dica =='sim':
    r1=random.randint (3,18)
    r2=random.randint(3,18)
    r3=random.randint(3,18)
    print(r1)
    print(r2)
    print(r3)
    if r1==soma or r2==soma or r3==soma:
        print("Está entre os 3")
        dinheiro = dinheiro-1
     
    else:
        print("Não está entre os 3")
        dinheiro = dinheiro-1
        dica = input('quer uma dica?' )
if dinheiro = 0:
    print ('você perdeu')
print(dinheiro)
while dinheiro > 0:
    resposta = int(input('qual seu chute?' ))
    if resposta = soma:
        print (dinheiro + 5*dinheiro)
        print('Você ganhou o jogo com  {0}!').format {dinheiro}
    else:
        dinheiro = dinheiro -1
if dinheiro = 0:
    print("Você perdeu!")
    
    
    
    
    