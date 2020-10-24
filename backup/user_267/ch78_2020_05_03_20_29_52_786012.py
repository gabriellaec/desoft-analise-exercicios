digite = input('Digite a aceleração: ')
if digite == 'sair':
    break    
while digite != 'sair':
    def calcula_tempo(dicio):
    nome_tempo = {}
    for e,a in dicio.items():
        t = (200/a)**(1/2)
        nome_tempo[e] = t
    if nome_tempo[e] >= nome_tempo[e+1]:
        vencedor = e
        tempo = t
    digite = input('Digite a aceleração: ')
    print('O vencedor é {0} com tempo de conclusão de {1} s'. format(vencedor ,tempo))
    
    
    