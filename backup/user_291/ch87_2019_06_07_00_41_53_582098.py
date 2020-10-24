with open('churras.txt', 'r') as arquivo:
    custo = 0
    for line in arquivo:
        coisas = line.split(',')
        quantidade = int(coisas[1])
        preço = float(coisas[2])
        tot = quantidade * preço 
        custo += tot

print(custo)
        