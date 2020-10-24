def calcula_tempo(atletas):
    final = {} 
    for k, v in atletas.items():
        tempo=100/v
        final[k]=tempo
    return final
print(calcula_tempo(atletas))