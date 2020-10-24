distancia=int(input('Qual a distancia deseja percorrer?   '))

def distancia_km(x):
    if x <= 200:
        d= x * 0.5
        return d
    else:
        d2=100+(x -200)*0.45
        return d2


print ('O total da sua passagem sera: {0:.2f} reais' .format(distancia_km(distancia)))