import math

sin = []
for i in range(90):
    sin.append(math.sin(i))
    
sin2 = []
for i in range(90):
    sin2.append((4*i*(180-i))/(40500-i*(180-i)))

erro = []
for i in range(len(sin2)):
    erro.append(sin2[i]-sin[i])

print(max(erro))