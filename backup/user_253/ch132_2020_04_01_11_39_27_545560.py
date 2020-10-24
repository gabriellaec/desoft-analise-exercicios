import math
def calcula_trabalho ( Força, O, distancia):
    O = math.radians(O)
    T= (math.cos(O)) *distancia*Força
    return T