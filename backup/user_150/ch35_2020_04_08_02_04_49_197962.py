soma = 0
pergunta1 = True

while pergunta1 == True:
    pergunta = float(input('Digite um número: '))
    if pergunta == 0:
        pergunta1 = False
    else:
        soma += pergunta
        
print(soma)