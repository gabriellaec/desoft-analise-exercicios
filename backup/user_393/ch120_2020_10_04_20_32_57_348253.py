import math
from random import *

dinheiro= 100
x= 1
lista= []
while x < 37:
    lista.append(x)
    x= x + 1

valor_aposta= int(input("Quanto vai apostar:"))
 

while dinheiro != 0:
    aposta= input("Qual a aposta:")
    if aposta== 'n':
        numero= int(input("Escolha um número:"))
        k= random.randit(lista)
        if k== numero:
            dinheiro= dinheiro + 35*valor_aposta
        else:
            dinheiro= dinheiro - valor_aposta
    if aposta== 'p':
        k= random.randit(lista)
        if k%2 == 0:
            dinheiro= dinheiro + valor_aposta
        else:
            dinheiro= dinheiro - valor_aposta
    if aposta== 'i':
        k= random.randit(lista)
        if k%2 != 0:
            dinheiro= dinheiro + valor_aposta
        else:
            dinheiro= dinheiro - valor_aposta
    print(dinheiro)
        