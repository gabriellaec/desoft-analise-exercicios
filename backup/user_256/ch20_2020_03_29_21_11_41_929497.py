distancia=int(input("Qual a distancia? "))
if distancia <=200:
    p1=0.50*distancia
    print(round(p1, 2))
elif distancia >200:
    p1=0.45*distancia
    print(p1)