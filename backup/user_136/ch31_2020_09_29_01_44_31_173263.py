controle= True
def  eh_primo(numero):
    while controle:
        if numero%2 == 0 or numero== 2:
            return True
        else:
            return False

w= int(input('qual o número ? '))
print (eh_primo(w))