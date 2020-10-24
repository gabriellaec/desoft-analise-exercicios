def distancia(ang,vel):
    import math
    dist=((vel**2)*(math.sin(2*ang)))/9.8
    
    if 98<dist and dist<102:
    	return( 'Acertou!')
    elif dist>=102:
    	return('Muito longe')
    else:
        return('Muito perto')

ang=float(input("insira o angulo de lançamento: "))
vel=float(input("insira a velocidade inicial do lançamento: "))
print(distancia(ang,vel))
