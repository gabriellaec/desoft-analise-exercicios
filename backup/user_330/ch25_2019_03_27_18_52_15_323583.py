def distancia(km):
    if km > 200 :
        resultado = 200*0.5 + (200-km)*0.45
        return resultado
    elif km <= 200:
        resultado = km*0.5
        return resultado