import math
dic = {}
while True: 

    a = input('a:')
    if a != 'sair':
        dic[a] = int(input('b:'))
    else:
        break

def calcula_tempo(a):
    for atleta in a:
        a[atleta] = math.sqrt(200/float(a[atleta]))
    return a
    
x = calcula_tempo(dic)
all_values = x.values()
min_value = min(all_values)


for each in x:

    if dic[each] == min_value:
        print('O vencedor é {} com tempo de conclusão de {} s'.format(each, min_value))
        