with open ('churras.txt', 'r') as arquivo:
    leitura = arquivo.readlines()
    total=0
    for lines in leitura:
        l = lines.split(',')
        mult = int(l[1])*float(l[2])
        total+=mult
    print(total)