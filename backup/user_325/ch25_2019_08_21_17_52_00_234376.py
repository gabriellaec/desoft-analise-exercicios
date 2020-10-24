distancia_txt = input("digite a distancia em km")
distancia_num = float(distancia_txt)

def calcula(distancia):
    
    if distancia <= 200:
        p = 0.5 * distancia
        return p
    else:
        p = 100 + (0.45 * (distancia - 200))
        return p
print("{0:.2f}".format(calcula(distancia_num)))
