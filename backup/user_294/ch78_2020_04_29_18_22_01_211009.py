def calcula_tempo(dicionario_de_atletas):
    dic_nome_tempo={}
    for nome in dicionario_de_atletas:
        tempo= (200/dicionario_de_atletas[nome])**(1/2)
        dic_nome_tempo[nome]=tempo
    return dic_nome_tempo

 

nome=input('qual é o seu nome?')
aceleracao=float(input('qual é a sua aceleracao?'))
dicionario_usu={}

 

while nome!='sair':
    nome=input('qual é o seu nome?')
    if nome=='sair':
        break
    aceleracao=float(input('qual é a sua aceleracao?'))
    dicionario_usu[nome]=aceleracao

 

    
dic_vencedor=calcula_tempo(dicionario_usu)
tempo_inicial=-1
for i in dic_vencedor:
    if tempo_inicial<0 or dic_vencedor[i]<tempo_inicial:
        tempo_inicial= dic_vencedor[i]
        nome_vencedor= i
print('O vencedor é {0} com tempo de conclusão de {1}'.format(nome_vencedor,tempo_inicial))