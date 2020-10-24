pergunta = float(input('Digite a distância a ser percorrida em km: '))
def calcula_passagem(x):
    if x <= 200:
        resultado = x * 0.5
    else:
        resultado = (x - 200) * 0.45 + 100
    y = print('O preço da sua passagem será: R$ {:.2f}'.format(resultado))
    return y
calcula_passagem(pergunta)