import math

def jacas(v, d):
    d = ((v**2)*math.sin(2*angulo)/9.8)
		if d < 98:
    		print('Muito perto')
				elif d > 102:
    				print('Muito longe')
						else: 
  							print('Acertou!')
    