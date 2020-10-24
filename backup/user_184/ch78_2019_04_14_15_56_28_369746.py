import math
def calcula_tempo (dic_atletas):
    conclusao = {}
    for atletas in dic_atletas:
        acc = dic_atletas[atletas]
        tempo = math.sqrt(200/acc)
        conclusao[atletas] = tempo
    return conclusao

nome = ''
aceleracao = 0
dicionario = {}

while nome != 'sair':
    nome = input('nome do atleta ')
    if nome != 'sair':
        aceleracao = float(input('acelearacao do atleta '))
        dicionario[nome] = aceleracao

        
menor = 99999999999
vencedor = ''
tconc = calcula_tempo(dicionario)
for atleta in tconc:
    if tconc[atleta] < menor:
        menor = tconc[atleta]
        vencedor = atleta

print ('O vencedor é {0} com tempo de conclusão de {1} s'.format(vencedor,menor))