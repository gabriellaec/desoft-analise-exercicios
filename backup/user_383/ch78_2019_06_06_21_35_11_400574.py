resposta = input('Você deseja adicionar mais nomes a competição?')
dic={}
menor = 10000000000
while resposta != 'sair':
    if resposta != 'sair':
        a = float(input('Qual a aceleração de cada corredor?'))
        dic[resposta] = a
    resposta = input('Você deseja adicionar mais nomes a competição?')
tempo = calcula_tempo(dic)
for k,v in tempo.items():
    if v < menor:
        menor = v
        chave = k
print('O vencedor é {} com o tempo de conclusão de {} s'.format(chave,menor))
