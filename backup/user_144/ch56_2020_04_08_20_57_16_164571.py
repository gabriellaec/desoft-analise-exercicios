#def calcula_norma(lista):
 #   norma = 0
  #  for i in range(len(lista)):
   #     norma = abs(lista[i])
        
    #return norma
        
    
from math import sqrt
def calcula_norma(lista):
    teste = []
    for i in range(len(lista)):
        teste.append(lista[i]**2)
    return sqrt(sum(teste))