def calcula_tempo(dicionario):
    tempo_conclusao=0
    Sf=100
    dicionario2={}
    for k,v in dicionario.items():
        tempo_conclusao=((2*Sf)/v)**(1/2)
        dicionario2[k]=tempo_conclusao
    return dicionario2