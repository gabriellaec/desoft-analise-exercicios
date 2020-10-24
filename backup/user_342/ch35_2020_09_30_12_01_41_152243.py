numero = True
soma=0
while numero:
    numero_escolhido= int(input('digite um numero:'))
    numero=True
    
    if numero_escolhido == 0:
        print(soma)
        numero=False
    else:
        numero=True
        soma=soma + numero_escolhido