def calcula_tempo(dicionario):
    dic={}
    for atleta, a in dicionario.items():
        t=(200/a)**0.5
        dic[atleta]=t
    return dic
at=input('nome atleta: ')

while at!='sair':
    new={}
    if at in dic.keys():
        new[at]=dic[at]
    return at
print('O vencedor é' + atleta+ 'com tempo de conclusão de ' + tempo' s'.format(atleta, t)

