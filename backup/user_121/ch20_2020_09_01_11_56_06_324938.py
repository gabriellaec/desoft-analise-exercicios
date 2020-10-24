pergunta = float(input('Digite a distância a ser percorrida em km: '))
def calcula_passagem(x):
    if x <= 200:
        resultado = x * 0.5
    else:
        resultado = 100 + x * 0.45
    y = print(resultado)
    return y
calcula_passagem(pergunta)