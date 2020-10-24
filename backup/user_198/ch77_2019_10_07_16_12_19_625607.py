import math

def calcula_tempo(atletas):
    tempo={}
    for nome in atletas:
        t=math.sqrt(200/atletas[nome])
        tempo[nome]=t
    return tempo
        
    
    