with open('churras.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    valor = 0
    for linha in linhas:
        l = linha.split(',')
        l[1].strip()
        l[2].strip()
        print(l)
#        valor += int(l[1]) * int(l[2])
        
print(valor)