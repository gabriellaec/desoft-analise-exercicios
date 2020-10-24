from math import sqrt
def calcula_tempo(dicionario):
	tempos = {} 
	for i in dicionario: 
		tempos[i] = sqrt(200/dicionario[i])
	return tempos 
nome = input('Digite seu nome: ')
valores = int(input('Digite sua aceleracao')) 
while nome != 'sair':
    nome = input('Digite seu nome: ')
    valores = int(input('Digite sua aceleracao'))
    if nome = 'sair':
        print('Ate a proxima')
        

    
    