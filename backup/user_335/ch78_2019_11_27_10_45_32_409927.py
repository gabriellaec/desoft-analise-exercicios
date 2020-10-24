def calcula_tempo(dicioAtletas):
    AtletaETempo = {}
    for atleta in dicioAtletas:
        if atleta != "sair":
            aceleracao = dicioAtletas[atleta]
            TempoDeProva = (200/aceleracao)**0.5
            AtletaETempo[atleta] = TempoDeProva
    return AtletaETempo

dicio = {"Barbara":10, "Raquel":5, "Lucas": 7.5, "Mimi":5, }
print (calcula_tempo(dicio))

vencedor = 0
tempo = 100000000

for n in dicio:
    if n != "sair":
        if dicio[n] < tempo:
            tempo = dicio[n]
            vencedor = n


print ('O vencedor é {0} com tempo de conclusão de {1} s'.format(vencedor,tempo))

