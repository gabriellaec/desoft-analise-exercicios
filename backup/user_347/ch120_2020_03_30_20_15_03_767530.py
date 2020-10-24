import random

 

dinheiro=100
print(dinheiro)
while dinheiro>0:
    aposta=int(input('Quanto você quer apostar? '))
    if aposta==0:
        break
    pergunta=input('número ou paridade?(n/p) ')
    if pergunta=='n':
        num=int(input('Escreva um número de 1 a 36 '))
        if num==random.randint(1,36):
            print(dinheiro+aposta*35)
            dinheiro=dinheiro+aposta*35
        else:
            print(dinheiro-aposta)
            dinheiro-=aposta
    
    if pergunta=='p':
        opções=input('par ou impar? ')
        if opções==random.choice(['par','impar']):
            print(dinheiro+aposta)
            dinheiro+=aposta
        else:
            print(dinheiro-aposta)
            dinheiro-=aposta