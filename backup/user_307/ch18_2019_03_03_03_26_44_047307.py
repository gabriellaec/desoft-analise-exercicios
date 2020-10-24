#Faça uma função que recebe a medida de um dos catetos e da hipotenusa de um 
#triângulo retângulo e devolve o valor do outro cateto.
#O nome da sua função deve ser encontra_cateto.
import math

cateto1=3
hipotenusa=5

def encontra_cateto(cateto1,hipotenusa):
	y=math.sqrt(hipotenusa**2-cateto1**2)
	return y
print(encontra_cateto(cateto1,hipotenusa))