distancia_km = float(input("Deseja percorrer quantos km: "))
if distancia_km <= 200:
    p = 0.5*distancia_km
    return {0}.format(.2f p)
else:
    preco = 100 + 0.45*distancia_km
    return {0}.format(.2f preco)