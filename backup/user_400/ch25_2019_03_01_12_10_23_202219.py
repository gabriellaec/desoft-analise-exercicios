distancia = int(input())
if distancia > 200:
    print(round((distancia-200)*0.45+100, 2))
else:
    print(round(distancia*0.5), 2)