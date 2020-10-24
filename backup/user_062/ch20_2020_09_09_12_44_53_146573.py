def f(d):
    if d <= 200:
        p = d*0.5
    elif d >= 200:
        p = 200*0.5 + (d-200)*0.45
    return p
d = float(input('Qual a distância que deseja percorrer?'))
print('O preço a pagar é: {:.2f}'.format(f(d)))