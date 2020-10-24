import math
def calcula_elongacao( amplitude, finicial, vel, tempo ):
     w = vel * (3.14/180)
     fase = finicial * (3.14/180)
     cos=math.cos
     return amplitude * cos( fase + (w * tempo) )
amplitude=1
fase=0
w=1
tempo=1.57
print (calcula_elongacao(amplitude, fase, w, tempo))
