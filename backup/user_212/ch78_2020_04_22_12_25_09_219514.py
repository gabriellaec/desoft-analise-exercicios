dic_atletas={}
nome=str(input('Qual o nome do atleta ?')
                       
while nome != 'sair':
    dic_atletas[nome]=int(input('Qual foi a aceleração do atleta?')
    nome=str(input('Qual o nome do atleta ?')
    
def calcula_tempo (dic_atletas):
    dic_tempo={}
    for a in dic_atletas:
        dic_tempo[a]=(200/(dic_atletas[a]))**(1/2)
    return dic_tempo
             
dicionario_tempo=calcula_tempo(dic_atletas)

menor_tempo=list(dicionario_tempo.values())[0]
melhor_atleta=list(dicionario_tempo.keys())[0]
for atleta,tempo in dicionario_tempo.items():
    if tempo < menor_tempo :
        menor_tempo=tempo
        melhor_atleta=atleta
             
print(f'O vencedor é {melhor_atleta} com tempo de conclusão de {menor_tempo} s')        