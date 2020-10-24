with open('churras.txt', 'r') as arquivo:
    valor_total = 0
    linhas = arquivo.readlines() #['linha1', 'linha2', ...]
    for linha in linhas:
        X = linha.split(',') #['carvao', '2', '9.90']
        A = float(X[1])
        B = float(X[2])
        valor = A*B
        valor_total += valor
    print(valor_total)
    
    
    