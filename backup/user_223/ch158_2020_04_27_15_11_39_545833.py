with open('texto.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    sem_espacos = linhas.strip()
    separado = sem_espacos.split()
    quant_palavras=0
    for e in separado:
        quant_palavras += len(e)
    print (quant_palavras)