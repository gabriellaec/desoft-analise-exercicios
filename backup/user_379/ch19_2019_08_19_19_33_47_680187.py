import math
def calcula_distancia_do_projetil(vel,teta,Y0):
    g=9.8
    tmp1=(vel**2)/(2*g)
    tmp2=(2*g*Y0)/(vel**2)*(math.sin(teta))**2
    tmp3=1+math.sqrt(1+tmp3)
	tmp4=math.sin(2*teta)
	return tmp1*tmp2*tmp4