resposta = True
while resposta:
    pergunta = input('Qual a senha?: ')
    if pergunta != 'desisto':
        pergunta = input('Qual a senha?: ')
        resposta = True
    else:
        resposta = False
        
print('Você acertou a senha!')