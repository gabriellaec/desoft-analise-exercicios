def onibus(distancia):
    
    if distancia <= 200:
        p = 0.5 * distancia
        return p
    else:
        p = 90 + 0.45 * distancia
        return p 
    
custo = onibus(350)
    
print("preco é {0:.2f}".format(custo))      