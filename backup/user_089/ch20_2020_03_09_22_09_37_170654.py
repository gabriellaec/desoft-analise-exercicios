distancia = input("Que distancia voce deseja percorrer em km?")


if (float(distancia)) <= 200:
    A= (float(distancia)*0.5)
    print (float("{0.:2f}")).format(A)


if (float(distancia)) > 200:
    B= (200*0.5 + (float(distancia)-200)*0.45)
    print (float('{.:2f}')).format(B)
