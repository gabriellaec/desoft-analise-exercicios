import random

dinheiro=100
dado=random.randint(1,36)
while dinheiro>0:
    print(dinheiro)
    aposta=int(input('Quanto você quer apostar? '))
    if aposta==0:
        break
    pergunta=input('número ou paridade?(n/p) ')
    if pergunta=='n':
        num=int(input('Escreva um número de 1 a 36 '))
        if num==dado:
            dinheiro=dinheiro+aposta*35
        else:
            dinheiro-=aposta
    
    if pergunta=='p':
        opções=input('par ou impar? ')
        if dado%2 == 0:
            resposta='p'
        else:
            resposta= 'i'
        if opções==resposta:
            dinheiro+=aposta
        else:
            dinheiro-=aposta
   


    
   


