km=int(input('Insira a distância (km) percorrida: '))
hs=int(input('Insira o tempo (h) decorrido: '))

def calcula_velocidade_media(a,b):
	return a/b

vm=calcula_velocidade_media(km,hs)
print(vm)