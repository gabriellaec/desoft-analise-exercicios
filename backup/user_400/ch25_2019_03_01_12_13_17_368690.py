distancia = int(input())
if distancia > 200:
    print("%.2f" % float((distancia-200)*0.45+100))
else:
    print("%.2f" % float(distancia*0.5))
    