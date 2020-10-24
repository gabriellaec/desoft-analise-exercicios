distancia = float(input())

if distancia > 200:
    print('R$ {:.2f}'.format(200*0.5 + (distancia-200)*0.45))
else:
    print('R$ {:.2f}'.format(distancia*0.5))