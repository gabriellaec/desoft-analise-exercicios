import math 
def calcula_tempo(a):
    for atleta in a:
        a[atleta] = math.sqrt(200/float(a[atleta]))
    return a