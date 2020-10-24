import math
def calcula_tempo(atletas):
    atletas = dict()
    atletas2 = dict()
    for nome, aceleracao in atletas.items():
        acel = float(aceleracao)
        atletas2[nome] = math.sqrt(200/acel)
    return atletas2
                        
            
    