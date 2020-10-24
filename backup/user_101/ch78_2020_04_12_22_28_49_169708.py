def calcula_tempo(dic_atletas):
    dic = {}
    for k, v in dic_atletas.items():
        a = int(v)
        d = 100
        t = (2*d/a)**(1/2)
        dic[k] = t
    return dic

nome = input('Qual o nome do atleta? ')
dic_fora = {}
while nome != 'sair':
    a = input('Qual a aceleração do atleta? ')
    dic_fora[nome] = a
    nome = input('Qual o nome do atleta? ')

t = calcula_tempo(dic_fora)
t_min = 0
nome = ' '
for k, v in t.items():
    if v < t_min:
        nome = k
        t_min = v

print('O vencedor é {0} com tempo de conclusão de {1} s'.format(nome, t_min))
    