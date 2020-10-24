def calcula_tempo(dicionario_atletas):
	nome_tempo = dict()
	for nome in dicionario_atletas:
		tempo = (2*100/dicionario_atletas[nome])**(1/2)
		nome_tempo[nome] = tempo
	return nome_tempo

nome = input('Diga o nome de um competidor: ')
aceleracao = float(input('Diga uma aceleracao: '))
novo_dic = {nome: aceleracao}

while nome != 'sair':
    nome = input('Diga outro nome de um competidor: ')
    if nome == 'sair':
        break
    else:
        aceleracao = float(input('Diga outra aceleracao: '))
        novo_dic[nome] = aceleracao

nome_tempo = calcula_tempo(novo_dic)
melhor_tempo = 1e8
melhor_competidor = ''
if nome_tempo[nome] < melhor_tempo:
    nome_tempo[nome] = melhor_tempo
    melhor_competidor = nome
    
print('O vencedor é {0} com tempo de conclusao de {1} s'.format(melhor_competidor, melhor_tempo))
        
                           
                   

