def calcula_tempo(atletas):
    atletas_tempo={}
    for c in atletas:
        atletas_tempo[c]=(200/atletas[c])**(1/2)
    return atletas_tempo
        