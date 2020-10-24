def calcula_preco_de_passagem (distancia_km):
    if (distancia_km <= 200):
        total = 0.5 * distancia_km
        return(total)
    else:
        total = (0.5 * 200) + ((distancia_km - 200)*0.45)
        return(total)

