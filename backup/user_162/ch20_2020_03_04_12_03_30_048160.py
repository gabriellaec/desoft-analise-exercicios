km = int(input("Distancia percorrida: "))
kmextra = 100 + (km - 200)*0.45
if km <= 200: 
    print("Voce deve {:.2f}".format(km*0.5))
else:
    print("Voce deve {:.2f}".format(kmextra))
    