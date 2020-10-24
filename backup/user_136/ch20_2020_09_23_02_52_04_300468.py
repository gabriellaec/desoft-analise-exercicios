def valor(d):
    if d <=200:
        preco= d * 0.5
        return ('o valor será de {0:.2f}'. format(preco))
    elif d>200:
        preco= 100 + ((d-200)*0.45)
        return ('o valor será de {0:.2f}'. format(preco))

w= int(input('Qual a distância ? '))
print(valor(w))
    