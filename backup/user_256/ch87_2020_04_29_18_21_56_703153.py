with open ('churras.txt', 'r') as arquivo:
    leitura = arquivo.readlines()
    total=0
    for lines in leitura:
        l = lines.split(',')
        mult = l[1]*l[2]
        total+=mult
    print(total)