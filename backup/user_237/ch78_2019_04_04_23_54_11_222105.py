programa = True
atletas = {}
while programa == True:
    nome = input("Qual é o nome?:")
    if nome == "sair":
        programa = False
    else:
    	aceleracao = float(input("Aceleracao?:"))
		atletas[nome] = aceleracao

def vencedor(t1):
    lista_tempos = t1.values()
    lista_atletas = t1.keys()
    menor_tempo = lista_tempos[0]
    melhor_atleta = lista_atletas[0]
    for t in range(0,len(lista_tempo)):
        
        if lista_tempo[t] < menor_tempo:
            menor_tempo = lista_tempo[t]
            melhor_atleta = lista_atletas[t]
    
    return ('O vencedor é {0} com tempo de conclusão de {1}'.format(melhor_atleta, menor_tempo))
        
                           



def calcula_tempo(atletas):
    tempos = {}
    for k,v in atletas.items():
        tempos[k] = (200/v)**(0.5)
    return tempos