atletas = {'Paulo': 10.0,'Pedro':5,'Lucas':4,'Thiago':2,'Joao':7}
def calcula_tempo(atletas):
    final = {} 
    for k, v in atletas.items():
        tempo=100/v
        final[k]=tempo
    return final
print(calcula_tempo(atletas))