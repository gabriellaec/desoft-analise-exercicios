distan = int(input('Digite a distância: '))

if distan <= 200:
    preco = distan * 0.5
else:
    preco = distan * 0.45

print('{:.02f}'.format(preco))