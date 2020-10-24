def calcula_tempo(atletas):
    tempo={}
    for nome,aceleraçao in atletas.items():
        a=int(aceleraçao)
        t=(200/a)**0.5
        tempo [nome]=t
    return tempo

dicionario={}
nomes=input('qual o nome do atleta: ')
while nomes!='sair':
    aceleraçao=int(input('qual a aceleraçao? '))
    dicionario[nomes]=aceleraçao
    nomes=input('qual o nome do atleta: ')
vence=calcula_tempo(dicionario)

for nome,tempo in vence.items():
    atleta=''
    menor=tempo[0]
    if tempo<menor:
        menor=tempo
        atleta=nome
print('O vencedor é {0} com tempo de conclusão de {1}s'.format(atleta, menor))