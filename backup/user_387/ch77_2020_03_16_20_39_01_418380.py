import math 
def calcula_tempo(a):
    for atleta in a:
        a[atleta] = math.sqrt(100/float(a[atleta]))
    return a