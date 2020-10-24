dist = float(input("Distancia que deseja percorrer em Km: "))
if dist <= 200:
    print("{0:.2f}".format(dist*0.5))
else:
    print("{0:.2f}".format(200*0.5 + (dist-200)*0.45))