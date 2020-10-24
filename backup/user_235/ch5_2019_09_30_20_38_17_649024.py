from math import *
def testa_primo(x): #retorna True se o número  for primo
    d = 2
    primo = True
    while d <= int(sqrt(x)):
        if x % d == 0:
            primo = False
            break
        elif x < 3:
            primo = False
        else:
            primo = True
            d = d + 1
    return primo
        
        
def maior_primo(x):
    num = int(x)
    if int(x) <= 1:
        return -1
    while testa_primo(num) == False:
        num = num - 1
    return num