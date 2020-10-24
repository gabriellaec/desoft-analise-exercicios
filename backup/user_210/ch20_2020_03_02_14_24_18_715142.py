distancia = float(input())
if distancia <= 200:
    print(distancia*0.5)
else:
    print(distancia*0.5 + (distancia-200)*0.45)