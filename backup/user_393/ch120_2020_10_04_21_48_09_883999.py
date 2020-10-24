import math
import random

dinheiro= 100
print('Você tem R${0}'.format(dinheiro))

 
while True:
    valor_aposta= int(input("Quanto vai apostar:"))
    if valor_aposta > dinheiro:
        print("Você não tem essa quantia de dinheiro")
        break
    if valor_aposta== 0:
        print("Você não quer mais apostar?! Ok,Obrigado por jogar!")
        break
    if dinheiro== 0:
        print("Acabou seu dinheiro!")
        break
    aposta= input("Qual a aposta:")
    if aposta== 'n':
        numero= int(input("Escolha um número:"))
        k= random.randint(1,36)
        if k== numero:
            dinheiro= dinheiro + 35*valor_aposta
        else:
            dinheiro= dinheiro - valor_aposta
    if aposta== 'p':
        x= input("Par ou Ímpar:")
        if x== 'p':
            k= random.randint(1,36)
            if k%2 == 0:
                dinheiro= dinheiro + valor_aposta
            else:
                dinheiro= dinheiro - valor_aposta
        if x== 'i':
            k= random.randint(1,36)
            if k%2 != 0:
                dinheiro= dinheiro + valor_aposta
            else:
                dinheiro= dinheiro - valor_aposta
     
 
    print("Agora você tem R${0}".format(dinheiro))
        

 