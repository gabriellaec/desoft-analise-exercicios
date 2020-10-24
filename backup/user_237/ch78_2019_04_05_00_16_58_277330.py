def vencedor(t1):
    
    melhor_atleta = min(t1, key = lambda x: t1.get(x) )
    menor_tempo = t1[melhor_atleta]
    
    
    return ('O vencedor é {0} com tempo de conclusão de {1}'.format(melhor_atleta, menor_tempo))
        
                           



def calcula_tempo(atletas):
    tempos = {}
    for k,v in atletas.items():
        tempos[k] = (200/v)**(0.5)
    return tempos








programa = True
atletas = {}
while programa == True:
    nome = input("Qual é o nome?:")
    if nome == "sair":
        programa = False
        
    else:
        aceleracao = float(input("Aceleracao?:"))
        atletas[nome] = aceleracao

tempos = calcula_tempo(atletas)
print(vencedor(tempos))
        
        
        
        

