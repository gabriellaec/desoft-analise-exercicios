dicionario={}
nomes=input('qual o nome do atleta: ')
while nome!='sair':
    aceleraçao=int(input('qual a aceleraçao? '))
    dicionario[nomes]=aceleraçao
    nomes=input('qual o nome do atleta: ')
vence=calcula_tempo(dicionario)
atleta=''
menor=tempo[0]
for nome,tempo in vence.items():
    if tempo<menor:
        menor=tempo
        atleta=nome
print('O vencedor é {0} com tempo de conclusão de {1}s'.format(atleta, menor))