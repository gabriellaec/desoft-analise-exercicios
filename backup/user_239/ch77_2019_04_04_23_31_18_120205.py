def calcula_tempo(dic):
    t=0
    saida={}
    for atleta,acelera in dic.items():
        t=((200*acelera)**0.5)/acelera
        saida[atleta]=t
    return saida
