distan = float(input('Digite a distância: '))

if distan <= 200:
    preco = distan * 0.5
else:
    preco = distan * 0.45
return f'{preco:.02f}'