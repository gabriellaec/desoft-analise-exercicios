pergunta = input('Qual a senha?: ')
resposta = True
while resposta:
    if pergunta == 'desisto':
        resposta = True
    else:
        pergunta = str(input('Qual a senha?: '))
        resposta = False
        
print('Você acertou a senha!')