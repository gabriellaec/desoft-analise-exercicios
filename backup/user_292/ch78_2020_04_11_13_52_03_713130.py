import math
rt = {}
x = 0
while x<1:
    n = input('qual o nome do atleta: ')
    if n == 'sair':
        x+=1
    else:
        a = int(input('ace: '))
        rt[n]=a
tempoA = {}
for c,v in rt.items():
    t = math.sqrt(((100*2)/v))
    tempoA[c] = t
Y = 0
X = ''
for x,y in tempoA.items():
    if y > Y:
        Y = y 
        X = x
print('O vencedor é {0} com tempo de conclusão de {1} s'.format(X,Y))