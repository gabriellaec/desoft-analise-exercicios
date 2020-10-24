from math import *

maior_erro = 0
for x in range(91):
    
    sin_x = (4*x*(180-x))/(40500-x*(180-x))
    erro = abs(sin(x) - sin_x)
    
    if erro > maior_erro:
        maior_erro = erro
        
print(maior_erro)