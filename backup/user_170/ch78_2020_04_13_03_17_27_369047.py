import math
def calcula_tempo(atletas):
    tConclusao = {}
    for n,a in atletas.items():
        t = math.sqrt(200/a)
        tConclusao[n] = t
    return tConclusao

sair = False
atletas = {}
while sair == False:
    n = input('Entre com um nome: ')
    if n == 'sair':
        sair = True
        break
    a = float(input('Entre com o valor da aceleracao: '))
    atletas[n] = a

tConclusao = calcula_tempo(atletas)
key_vencedor = min(tConclusao, key = tConclusao.get)
print('O vencedor é {} com tempo de conclusão de {} s'.format(key_vencedor, tConclusao[key_vencedor]))

    



