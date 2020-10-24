D = int(input("A distancia que seseja percorer"))
if d <= 200:
    print(d*0.5)
else:
    print(100+((d-200)*0.45))