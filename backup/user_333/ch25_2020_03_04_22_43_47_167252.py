g=9.8

def distancia_projetil(v,teta):
    distancia=(v**2*math.sin(2*teta))/g
    if float(distancia)<98:
        resultado=str('Muito perto')
    elif 98<=float(distancia)<=102:
        resultado=str('Acertou!')
    else:
        resultado=str('Muito longe')
    return resultado

print(distancia_projetil(25,45))
