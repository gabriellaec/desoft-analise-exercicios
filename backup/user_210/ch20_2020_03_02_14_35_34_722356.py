distancia = float(input())
if distancia <= 200:
    print("{:.2f}".format(distancia*0.5))
else:
    print("{:.2f}".format(distancia*0.5 + (distancia-199)*0.45))