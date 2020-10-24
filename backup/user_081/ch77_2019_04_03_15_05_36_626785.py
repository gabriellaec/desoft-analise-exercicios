import math 

dicioatletas = dict()
dicioatletas['Bolt'] = 3
dicioatletas['Blake'] = 2.8
dicioatletas['Powell'] = 2.7
dicioatletas['Tyson gay'] = 2.91
dicioatletas['Eu'] = 10

def calcula_tempo(x):
    diciotempo = dict()
    for atletas in x:
        aceleracao = x[atletas]
        tempo = math.sqrt(200/aceleracao)
        diciotempo[atletas] = tempo
        
    print(diciotempo)