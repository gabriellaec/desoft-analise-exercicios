lista = []
with open('churras.txt','r') as arquivo:
    linhas = arquivo.read().split('\n')
    for i in range(len(linhas)):
        lista.append(linhas[i].split(','))
total = 0
for i in lista:
    total += float(i[1]) + float(i[2])
print(total)