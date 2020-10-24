jogo = True
import math

while jogo:
    a = input("Qual o nome?")
    if a == "sair":
        jogo = False
    else:
        b = float(input("Aceleracao?"))     
        dic = {a:b}
dic2 = {}
soma = 0
for e in dic:
    if e not in dic2:        
        dic2[e] = math.sqrt(200/dic[e])
        if dic2[e] > soma:
        soma = dic2[e]
    
r = ('O vencedor é {0} com tempo de conclusão de {1} s'.format(dic2[e],soma)
return r