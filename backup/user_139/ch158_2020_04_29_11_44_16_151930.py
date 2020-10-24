with open('arquivo_texto.txt', 'r') as arquivo:
    linhas = arquivo.read()
    a = linhas.split()
    b = len(a)
    print (a)