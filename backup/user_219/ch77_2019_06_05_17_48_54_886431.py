def calcula_tempo(atletas):
    nomes=[]
    tempo=[]
    for atleta in atletas:
        nomes.append(atleta)
    for ac in atletas.values():
        tempo.append((200/ac)**0.5)
    dict={}
    dict[nomes]= tempo
    return dict
        
    