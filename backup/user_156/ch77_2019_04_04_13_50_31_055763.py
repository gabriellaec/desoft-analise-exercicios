def calcula_tempo(dicionario):
    tempo_conclusao=0
    sf=100
    dicionario2={}
    for nome,aceleracao in dicionario.items():
        tempo_conclusao=((2*sf)/aceleracao)**(1/2)
        dicionario2[nome]:tempo_conclusao
    return dicionario2
print(calcula_tempo({'gian':10,'andre':5}))


     