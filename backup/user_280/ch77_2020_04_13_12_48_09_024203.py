def calcula_tempo(atletas):
    resultado = {}
    for atleta in atletas:
        if not atleta in resultado:
            resultado[atleta] = v/atletas[atleta]
    return resultado
      
    