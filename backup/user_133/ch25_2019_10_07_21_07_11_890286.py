distan = float(input('Digite a distancia: '))

if distan <= 200:
    preco = 0.5 * distan
else:
    preco = ((distanc - 200) * 0.45) + 100
    
print(f'{preco:.02f}')
    