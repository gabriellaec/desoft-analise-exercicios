i = 1
contador = 0
maior = 0
i = 1
contador = 0
maior = 0
resposta = 0
a = True
while i < 1000:
    while a:
        contador += 1
        if i == 1:
            a = False
            break
        elif i % 2:
            i = i/2
        else:
            i = 3 * i + 1
    if contador > maior:
        maior = contador
        resposta = i
    i += 1

print(resposta)