nome = ''
aceleracao = 0
dic_atletas = {}

while nome != 'sair':
    nome = input('Digite o nome do atleta: ')
    if nome != 'sair':
        aceleracao = int(input('Digite sua aceleração: '))
        dic_atletas[nome] = aceleracao
                         
def calcula_tempo(dic_atletas):
    dic = dic_atletas
    saida = {}
    for k,v in dic.items():
        saida[k] = (200/v)**(1/2)
    return saida
                         
dic_tempos = calcula_tempo(dic_atletas)
TEMPO = 1000
NOME = ''
for k,v in dic_tempos.items():
    if v < 1000:
        TEMPO = v
        NOME = k
print('O vencedor é {0} com tempo de conclusão de {1} s'.format(NOME,TEMPO))
              