pergunta = input('Digite a distância a ser percorrida em km: ')
def f(x):
    if x <= 200:
        resultado = x * 0.5
    else:
        resultado = 200 * 0.5 + x * 0.45
    return resultado
f(pergunta)