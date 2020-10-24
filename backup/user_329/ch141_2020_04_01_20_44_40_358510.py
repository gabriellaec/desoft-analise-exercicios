inicio = 1000
from random import randrange, uniform

aposta = input("Você quer apostar?")

if aposta == "não":
    print("O jogo acabou.")
if aposta !== "não":
    soma = int(input("quanto da a soma de dois dados?"))
    comp = print(randrange(1, 6), randrange(1, 6))
    inicio -= 30
    
    if soma == comp