velocidade= float(input('Digite a velocidade de sua jaca '))
angulo= float(input('Digite o angulo de lancamento de sua jaca ')) 
def distancia_jaca(velocidade,angulo): 
    g=9.8
    d=(velocidade**2)*sin(2*(angulo))/g
    if d==2:
        print('Acertou!') 
	elif d>2:
        prinnt('Muito longe') 
    else:
        print('Muito perto') 