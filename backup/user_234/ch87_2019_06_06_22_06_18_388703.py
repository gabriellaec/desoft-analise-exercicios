a = []

with open('churras.txt','r') as arquivo:
    churras = arquivo.read()
    lista = churras.split() and churras.split('\n')
    gasto =0
    for e in lista:
        a.append(e.split(','))
    for item in a:
        gasto += int(item[1])*float(item[2])
print(gasto)
        