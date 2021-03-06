from math import sin, pi

maior_erro = 0
angulo_erro = 0

def sin_bhaskara(graus):
    
    if graus > 90 or graus < 0: raise ValueError('Ângulos entre 0 e 90 graus apenas.')
    
    numerador = 4 * graus * (180 - graus)
    denominador = 40500 - graus * (180 - graus)
    
    return numerador / denominador
    

for angulo in range(0, 91):
    
    seno = sin(angulo * pi / 180)
    seno_bhaskara = sin_bhaskara(angulo)
    
    erro = abs(seno - seno_bhaskara)
    
    if erro > maior_erro:
        maior_erro = erro
        angulo_erro = angulo

print(angulo)