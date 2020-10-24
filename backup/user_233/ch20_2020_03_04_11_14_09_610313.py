distancia = float(input())

if distancia > 200: preco = (distancia - 200)  * 0.45 + 100
else: preco = distancia * 0.5
    
unidade = int(preco)
decimo = int(preco * 10 - unidade * 10)
centesimo = int(preco * 100 - decimo * 10 - unidade * 100)

print('%d,%d%d' % (unidade, decimo, centesimo))