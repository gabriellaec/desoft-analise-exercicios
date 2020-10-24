distan = float(input('Digite a distância: '))

if distan <= 200:
    preco = distan * 0.5
else:
    preco =  (distan -200) * 0.45 + 100
    
print('{:.02f}'.format(preco)