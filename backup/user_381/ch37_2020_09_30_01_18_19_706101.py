pergunta = str(input('Qual a senha?: '))
resposta = True
while resposta:
    if pergunta != 'desisto':
        pergunta = str(input('Qual a senha?: '))
        resposta = False
    else:
        resposta = True 
print('Você acertou a senha!')