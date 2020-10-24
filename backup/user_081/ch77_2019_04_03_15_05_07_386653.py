def calcula_tempo(x):
    diciotempo = dict()
    for atletas in x:
        aceleracao = x[atletas]
        tempo = math.sqrt(200/aceleracao)
        diciotempo[atletas] = tempo
        
    print(diciotempo)