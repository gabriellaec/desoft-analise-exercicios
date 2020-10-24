with open('churras.txt', 'r') as arquivo:
    c = arquivo.read()
    custo = 0
    for line in c:
        coisas = line.split(',')
        quantidade = int(coisas[1])
        preço = float(coisas[2])
        tot = quantidade * preço 
        custo += tot

print(custo)
        