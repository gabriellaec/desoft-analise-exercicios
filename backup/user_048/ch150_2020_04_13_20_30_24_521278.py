import math
def calcula_pi(n):
   produto=1
   termos=range(1,n+1)
   for o in termos:
     produto= produto+math.sqrt(6/(n**2))
   return produto