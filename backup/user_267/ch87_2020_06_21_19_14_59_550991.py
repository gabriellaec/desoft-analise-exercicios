with open('churras.txt','r') as arquivo:
    linhas = arquivo.readlines()
    total = 0
    for linha in linhas:
        total += linha[1]*linha[2]
    print(total)
    