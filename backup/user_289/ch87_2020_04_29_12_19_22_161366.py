with open('churras.txt', 'r') as arquivo:
    valor_total = 0
    linhas = arquivo.read()
    lista = linhas.split('
')
    termos = lista.split(',')
    i = 0
    for e in termos:
        A = float(termos[i+1])
        B = float(termos[i+2])
        i += 3
    valor = A*B
    valor_total += valor
    print(valor_total)
    
    
    