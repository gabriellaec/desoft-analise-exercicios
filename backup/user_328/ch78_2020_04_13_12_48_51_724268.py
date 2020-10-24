import math

def calcula_tempo(lista):
    dict= {}
    for k, v in lista.items():
        t = math.sqrt(200/v)
        dict[k] = t
        x = dict[k]
        nome = k
        for i in dict:
            if dict[i] < x:
                nome = i
                x = dict[i]
        final = 'O vencedor é {} com tempo de conclusão de {} s'.format(nome,x)
        return final
    
dict = {}
while True:
    nome = str(input('Digite o nome do atleta: '))
    if nome == 'sair':
        break
    ac = int(input('Qual é sua acelereção? '))
    dict[nome] = ac
    
    

