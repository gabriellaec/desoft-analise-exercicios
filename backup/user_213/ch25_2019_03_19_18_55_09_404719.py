distancia=float(input("qual distancia vc deseja percorrer em km?: "))
if distancia<=200:
    print(distancia*0.50)
else:
    print(200*0.50+(distancia-200)*0.45)