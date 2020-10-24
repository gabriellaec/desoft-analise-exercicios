soma=0
while True:
    resposta= int(input("escreva um número: "))
    if resposta == 0:
        break
    else:
        soma+=resposta
print(soma)