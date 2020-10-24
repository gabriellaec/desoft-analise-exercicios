import math
def calcula_tempo(atletas):
    atletas2 = dict()
    for nome, aceleracao in atletas.items():
        acel = float(aceleracao)
        tempo = math.sqrt(200/acel)
        atletas2[nome] = tempo
    return atletas2
                        
            
    