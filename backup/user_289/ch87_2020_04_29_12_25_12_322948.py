with open('churras.txt', 'r') as arquivo:
    valor_total = 0
    linhas = arquivo.readlines()#['linha1', 'linha2', ...]
    for elemento in linhas:
        X = elemento.split(',')
        i = 0
        for e in linhas:
            A = float(linhas[i+1])
            B = float(linhas[i+2])
            i += 3
    valor = A*B
    valor_total += valor
    print(valor_total)
    
    
    