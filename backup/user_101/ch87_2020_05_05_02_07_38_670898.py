with open('churras.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    valor = 0
    for linha in linhas:
        l = linha.split(',')
        l[1].replace('\n','')
        l[2].replace('\n','')
        valor += int(l[1])*int(l[2])
print(valor)