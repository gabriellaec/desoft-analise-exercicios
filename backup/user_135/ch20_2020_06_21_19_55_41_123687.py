distancia = int(input())

if distancia > 200:
    print('R${:.2f}'.format(distancia*0.45))
else:
    print('R${:.2f}'.format(distancia*0.5))