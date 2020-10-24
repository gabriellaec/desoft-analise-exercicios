resposta = input('Você deseja adicionar mais nomes a competição?')
dic={}
maior = 0
while resposta != 'sair':
    if resposta != 'sair':
		a = float(input('Qual a aceleração de cada corredor?'))
        dic[resposta]=a
    resposta = input('Você deseja adicionar mais nomes a competição?')
calcula_tempo(dic)
for k,v in dic.items():
    v = maior
    if v>maior:
        v=maior
print('O vencedor é {} com o tempo de conclusão de {} s'.format(k,v))
