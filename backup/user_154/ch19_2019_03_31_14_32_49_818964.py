import math

def calcula_distancia_do_projetil(v, teta, h):
    if v == 0.0 or math.sin(teta) == 0:
        return 0
    
    preparte = 1 + (16.9 * h)/(v**2 * math.sin(teta)**2)
    
    if preparte < 0:
        return 0
    
    parte1 = v**2 / 16.9
    parte2 = 1 + math.sqrt(preparte) 
    parte3 = math.sin(2 * teta)
    
    return parte1 * parte2 * parte3
    
v = float(input("Velocidade: "))
teta = float(input("Angulo: "))
h = float(input("Altura: "))
    
print(calcula_distancia_do_projetil(v, teta, h))