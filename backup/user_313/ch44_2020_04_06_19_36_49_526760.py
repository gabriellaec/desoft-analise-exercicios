meses = {'janeiro': 1,'fevereiro' : 2, 'março' : 3, 'abril' : 4, 'maio' : 5,'junho' : 6, 'julho' : 7,'agosto' : 8, 'setembro' : 9, 'outubro' : 10 ,'novembro' : 11,'dezembro' : 12}

pergunta = input('Qual o nome do mes ?')
if pergunta in meses:
    resposta = meses[pergunta]
    print('O numero do {} que você escreveu é {}'.format(pergunta,resposta))

else:
    print('Não existe numero para sua resposta')