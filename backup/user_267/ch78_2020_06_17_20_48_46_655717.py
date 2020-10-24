def calcula_tempo(dicio):
    nome_tempo = {}
    for e,a in dicio.items():
        t = (200/a)**(1/2)
        nome_tempo[e] = t
    return nome_tempo 

nome_acel = {}
nome = input('Digite o nome: ')
while nome != 'sair':
    digite = input('Digite a aceleração: ')
    nome_acel[nome] = digite
    nome = input('Digite o nome: ')

nova = calcula_tempo(nome_acel)
vencedor = ''
menor_tempo = 0
#t = float('inf')
for no_me,tem_po in nova.items():
    if tem_po < menor_tempo:
        vencedor = no_me
        tempo = tem_po
print('O vencedor é {0} com tempo de conclusão de {1} s'. format(vencedor ,tempo))
    


    
    