D = float(input("A distancia que seseja percorer"))
if D <= 200:
    print(round((D*0.5),2))
else:
    print(round(100+((D-200)*0.45),2))