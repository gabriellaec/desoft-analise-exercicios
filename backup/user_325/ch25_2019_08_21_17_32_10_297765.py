def onibus(distancia):
    
    if distancia <= 200:
        p = 0.5 * distancia
        return p
    else:
        P = 90 + 0.45 * distancia
        return p
        
print(onibus(500))