distan = float(input('Digite a distância: '))

if distan <= 200:
    preco = distan * 0.5
else:
    preco = distan * 0.45
print(f'{preco:.02f}')