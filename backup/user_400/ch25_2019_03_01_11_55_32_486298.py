distancia = int(input())
if distancia > 200:
    print(float((distancia-200)*0.45+100))
else:
    print(float(distancia*0.5))