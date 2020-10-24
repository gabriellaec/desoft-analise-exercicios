import math

mathsin = []
for i in range(91):
    mathsin.append(math.sin(math.radians(i)))

bhaskara = []
for i in range(91):
    bhaskara.append((4*i*(180-i))/(40500-i*(180-i)))

erro = []
for i in range(len(bhaskara)):
    erro.append(bhaskara[i]-mathsin[i])

novoerro = []
for i in range(len(erro)):
    novoerro.append(abs(erro[i]))
    
print(erro.index(max(novoerro)))