import math
def calcula_tempo(atletas):
    resultado = {}
    for atleta in atletas:
        if not atleta in resultado:
            resultado[atleta] = math.sqrt(200/atletas[atleta])
    return resultado
      
    