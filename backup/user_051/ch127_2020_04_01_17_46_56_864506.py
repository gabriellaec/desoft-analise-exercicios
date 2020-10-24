import math
def calcula_elongacao( amplitude, finicial, vel, tempo ):
     w = vel * (3.14/180)
     fase = finicial * (3.14/180)
     cos=math.cos
     return amplitude * cos( fase + (w * tempo) )
amplitude=0.5
fase=0
w=10
tempo=1
print (calcula_elongacao(amplitude, fase, w, tempo))