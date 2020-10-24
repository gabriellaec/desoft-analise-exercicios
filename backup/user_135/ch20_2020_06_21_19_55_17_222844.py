distancia = int(input())

if distancia > 200:
    print('{:.2f}'.format(distancia*0.45))
else:
    print('{:.2f}'.format(distancia*0.5))