def faixa_notas(lista):
    menor = 0
    medio = 0
    maior = 0
    i = 0
    while i < len(lista):
        if lista[i] < 5:
            menor += 1
        elif 5 <= lista[i] and lista[i] <= 7:
            medio += 1
        else:
            maior += 1
        i += 1
    resposta = [menor,medio,maior]
    return resposta