lista=[]
with open ('churras.txt', 'r') as churrastxt:
    linhas = churrastxt.readlines()
    for i in linhas:
        lista.append(i.split(','))
total = 0
for i in lista:
    total += int(i[1]) * float(i[2])
print(total)