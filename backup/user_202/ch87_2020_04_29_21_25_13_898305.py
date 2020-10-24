with open('churras.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    valor = 0
    for linha in linhas:
        palavra = linha.split(',')
        valor += int(palavra[1])*int(palavra[2])
    print(valor)