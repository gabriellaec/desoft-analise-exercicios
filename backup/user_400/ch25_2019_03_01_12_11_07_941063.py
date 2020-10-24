distancia = int(input())
if distancia > 200:
    print(round(float((distancia-200)*0.45+100), 2))
else:
    print(round(float(distancia*0.5)), 2)