distancia_km = int(input("Deseja percorrer quantos km"))
if distancia_km <= 200:
    p = 0.5*distancia_km
    return p
else:
    p = 100 + 0.45*distancia_km
    