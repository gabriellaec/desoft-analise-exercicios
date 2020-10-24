import random
import math
import string
import secrets

velmax = int(input('Qual é a velocidade máxima da via? '))
d = int(input('Qual é a distância entre as câmeras? '))

N = 7
placa = ''.join(secrets.choice(string.ascii_uppercase + string.digits) 
                                                  for i in range(N)) 

t= int(input('Quanto tempo entre as cameras?'))
vel = d/t

if v > velmax and v <= velmax*1.20:
    print('Infração média: multa de 130,16')
elif v > velmax*1.20 and v < velmax*1.5:
    print('Infração grave: multa de 195,23')
elif v > velmax*1.5:
    print('Infração gravissíma: multa de 585,69. Penalidade: suspensão imediata do direito de dirigir e apreensão do documento de habilitação.

             
