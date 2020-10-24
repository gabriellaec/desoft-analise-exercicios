distancia_km = float(input("Distancia: "))

if distancia_km <= 200:
    valorfinal = distancia_km*0.50
    print("{0:.2f}" .format(valorfinal))
else:
    valorfinal = 200*0.50
    valorfinal = (distancia_km-200)*0.45 + valorfinal
    print("{0:.2f}" .format(valorfinal))