def eh_primo(numero):
    i=0
    impar=1
    while i < numero:
        if numero == 2:
            resposta = 'True'
        elif numero % 2 ==0 or numero % impar == 0:
            resposta = 'False'
        else:
            resposta= 'True'
        i+=1
        impar+=2
    return resposta
primo=13
naoprimo=2
np=8
print(eh_primo(primo))
print(eh_primo(naoprimo))
print(eh_primo(np))