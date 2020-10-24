distancia=int(input("Qual a distancia? "))
if distancia <=200:
    p1=0.50*distancia
    print ('{0:.2f}.format(p1))
else:
    p2= (200*0.50) + 0.45*(distancia-200)
    print('{0:.2f}.format(p2))