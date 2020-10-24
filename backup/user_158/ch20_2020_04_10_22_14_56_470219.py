D = int(input("A distancia que seseja percorer"))
if D <= 200:
    print(D*0.5)
else:
    print(100+((D-200)*0.45))