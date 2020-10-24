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
t = float('inf')
for n,t in nova.items():
    if t[n] > t[n-1]:
        vencedor = n
        tempo = t
    
    
print('O vencedor é {0} com tempo de conclusão de {1} s'. format(vencedor ,tempo))
    


    
    