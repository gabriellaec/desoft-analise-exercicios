def calcula_tempo(d):
    new_d = {}
    for key,a in d.items():
        tempo = (200/a)**(1/2)
        new_d[key] = tempo
    return new_d
dic = calcula_tempo(d)
for k in d.keys():
    if i != 'sair':
        print('O vencedor é {0} com tempo de conclusão de {1}s'.format(k,dic[k]))
    else:
        pass
  