resposta = True
while resposta:
    pergunta = input('Qual a senha?: ')
    if pergunta == 'desisto':
        resposta = False
        
print('Você acertou a senha!')
