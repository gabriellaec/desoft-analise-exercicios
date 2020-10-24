with open ('churras.txt', 'r') as arquivo:
    leitura = arquivo.readlines()
    total=0
    for lines in leitura:
        mult = lines[1]*lines[2]
        total+=mult
    print(total)