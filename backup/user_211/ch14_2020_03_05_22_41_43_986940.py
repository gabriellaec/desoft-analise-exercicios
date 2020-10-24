import math
def calcula_distancia_do_projetil(v,teta,alt):
    parte_1=((v**2)/(2*9.8))
    parte_2=(1+math.sqrt(1+((2*9.8*alt)/((v**2)*(math.sin(teta)**2)))
    x=math.sin(2*teta)
	dist=parte1*parte2*x
                        
	return dist