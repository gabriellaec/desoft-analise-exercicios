distancia = input("Que distancia voce deseja percorrer em km?")
if int(distancia) <= 200:
    print(int(distancia)*0.5)
if int(distancia) > 200:
    print (200*0.5 + (int(distancia)-200)*0.45)