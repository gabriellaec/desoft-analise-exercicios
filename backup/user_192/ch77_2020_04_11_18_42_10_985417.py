import math
def calcula_tempo(atletas):
    atletas = dict()
    atletas2 = dict()
    for nome, aceleracao in atletas.items():
        atletas2[nome] = int(math.sqrt(200/aceleracao))
    return atletas2
                        
            
    