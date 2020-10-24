def calcula_tempo (dic):
    dic_f = {}
    for k, a in dic.items():
        t = (200/a)**(1/2)
        dic_f[k] = t
    return dic_f

while True:
    dic = {}
    n = input("Qual o nome do atleta? ")
    if n != 'sair':
        a = int(input("Qual a aceleracao do atleta? "))
        dic[n] = a
        continue
    else:
        dic_f = calcula_tempo(dic)
        vencedor = dic_f[min(dic_f, key = dic_f.get)]
        tempo = min(dic_f, key = dic_f.get)
        print("O vencedor é {0} com tempo de conclusão de {1} s".format(vencedor,tempo))
        break