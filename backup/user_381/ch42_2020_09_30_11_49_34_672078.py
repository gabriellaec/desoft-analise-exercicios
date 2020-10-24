resposta = True
while resposta:
    pergunta = input('Me diga uma palavra: ')
    if pergunta == 'fim':
        resposta = False
    elif pergunta[0] == 'a':
        print(pergunta)