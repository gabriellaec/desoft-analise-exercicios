with open ('churras.txt', 'r') as arquivo:
    leitura = arquivo.read()
    total=0
    for lines in leitura:
        mult = lines[0]*lines[1]
        total+=mult
    print(total)