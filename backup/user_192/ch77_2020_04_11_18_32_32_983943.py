import math
def calcula_tempo(atletas):
    atletas = dict()
    atletas2 = dict()
    for n, a in atletas.items():
        atletas2['n'] = int(math.sqrt(200/a))
    return atletas2
                        
            
    