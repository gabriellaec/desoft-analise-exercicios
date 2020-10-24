distancia = float(input ("Qual? "))
if distancia <= 200:
    print(distancia*0.5:.2f)
else:
    print(100+(distancia-200)*0.45:.2f)