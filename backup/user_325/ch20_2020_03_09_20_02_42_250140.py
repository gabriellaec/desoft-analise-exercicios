distancia = int(input("distancia em km "))
if distancia <= 200:
    p = 0.50*distancia
else:
    p = (0.45*(distancia-200))+100
