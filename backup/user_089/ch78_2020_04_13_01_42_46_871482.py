jogo = True
import math

while jogo:
    a = input("Qual o nome?")
    if a == "sair":
        break
    else:
        b = float(input("Aceleracao?"))     
        dic = {a:b}
        dic2 = {}
        for e in dic:
            dic2[e] = math.sqrt(200/dic[e])
            jogo = False
r = ('O vencedor é {0} com tempo de conclusão de {1} s'.format(a,dic2)
return r