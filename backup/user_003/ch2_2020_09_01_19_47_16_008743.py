

def calcula_velocidade_media(k,h) :
    velocidade = k / h
    return velocidade
    # velocidade calculada pela distancia percorrida em certo tempo



k = 100 #distancia em km

h = 10 #tempo em horas


v = calcula_velocidade_media(k,h)

print( "{0} km/h" .format( v ))