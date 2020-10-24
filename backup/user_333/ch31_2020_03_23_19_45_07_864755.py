"""
Teste para saber se o número é primo

@author: Francisco Janela
"""

def eh_primo(numero):
    if numero==1 or numero==0:
        return False
    elif numero==2:
        return True
    else:
        x=3
        while x<numero:
            if numero%x==0:
                break #serve para sair do while
            else:
                x+=2
        if numero==x:
            return True
        else:
            return False

print(eh_primo(373))