import math
def calcula_tempo(atletas):
    atletas_t={}
    for i in atletas:
        atletas_t[i]=math.sqrt(200/atletas[i])
    return atletas_t